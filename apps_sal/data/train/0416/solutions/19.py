class Solution:
    def catMouseGame(self, g: List[List[int]]) -> int:
        # observations:
        # we can represent the game state with the triplet (mouse cat turn).
        # (_ 0 _) is illegal.
        # (0 _ _) = 1 (mouse victory).
        # (x x _) = 2 (cat victory).
        # if any possible move leads to win, current state is win:
        # * (m c c) = 1 => (m' c m) = 1 for m' in g[m].
        # * (m c m) = 2 => (m c' c) = 2 for c' in g[c].
        # if all possible moves lead to loss, current state is loss.
        # * (m c m) = 1, for c' in g[c], if all((m c'' m) = 1 for c'' in g[c']) => (m c' c) = 1
        # * (m c c) = 2, for m' in g[m], if all((m'' c c) = 2 for m'' in g[m']) => (m' c m) = 2
        # return (1 2 m). return once we know its value.

        MTURN, CTURN = 0, 1
        ILLEGAL, UNKNOWN, MWIN, CWIN = -1, 0, 1, 2

        n = len(g)
        s = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        q = deque()

        def sq(m, c, t, v):
            if s[m][c][t] == UNKNOWN:
                q.append((m, c, t))
                s[m][c][t] = v

        # set and enqueue initial known states.
        for t in (MTURN, CTURN):
            for m in range(n):
                sq(m, 0, t, ILLEGAL)
            for c in range(n):
                sq(0, c, t, MWIN)
            for x in range(n):
                sq(x, x, t, CWIN)

        while q:
            m, c, t = state = q.popleft()

            # apply production rules. for each unencountered resultant state, set and enqueue.
            if t == CTURN and s[m][c][t] == MWIN:
                for m_ in g[m]:
                    sq(m_, c, MTURN, MWIN)

            if t == MTURN and s[m][c][t] == CWIN:
                for c_ in g[c]:
                    sq(m, c_, CTURN, CWIN)

            if t == MTURN and s[m][c][t] == MWIN:
                for c_ in g[c]:
                    if all(s[m][c__][MTURN] in (ILLEGAL, MWIN) for c__ in g[c_]):
                        sq(m, c_, CTURN, MWIN)

            if t == CTURN and s[m][c][t] == CWIN:
                for m_ in g[m]:
                    if all(s[m__][c][CTURN] in (ILLEGAL, CWIN) for m__ in g[m_]):
                        sq(m_, c, MTURN, CWIN)

            # once we know state[1,2,m], return it.
            if s[1][2][MTURN]:
                return s[1][2][MTURN]

        # everything else is a draw.
        return 0
