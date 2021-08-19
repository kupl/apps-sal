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
        # (m c m) = 1 and c not in g[m] => (m c c) = 1.
        # if all possible moves lead to loss, current state is loss.
        # * (m c m) = 1, for c' in g[c], if all((m c'' m) = 1 for c'' in g[c']) => (m c' c) = 1
        # return (1 2 m). return once we know its value.

        n = len(g)
        s = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        q = deque()

        def sq(m, c, t, v):
            if s[m][c][t] == 0:
                q.append((m, c, t))
                s[m][c][t] = v

        # approach:

        # set and enqueue initial known states.
        for m in range(n):
            for t in range(2):
                sq(m, 0, t, -1)
        for c in range(n):
            for t in range(2):
                sq(0, c, t, 1)
        for x in range(n):
            for t in range(2):
                sq(x, x, t, 2)

        # while queue:
        while q:
            # pop state.
            m, c, t = state = q.popleft()
            # apply production rules. for each unencountered resultant state, set and enqueue.
            if t == 1 and s[m][c][t] == 1:
                for m_ in g[m]:
                    sq(m_, c, 0, 1)

            if t == 0 and s[m][c][t] == 2:
                for c_ in g[c]:
                    sq(m, c_, 1, 2)

            # if t == 0 and s[m][c][t] == 1 and c not in g[m]:
            #     sq(m, c, 1, 1)

            if t == 0 and s[m][c][t] == 1:
                for c_ in g[c]:
                    if all(s[m][c__][0] in (-1, 1) for c__ in g[c_]):
                        sq(m, c_, 1, 1)

            if t == 1 and s[m][c][t] == 2:
                for m_ in g[m]:
                    if all(s[m__][c][1] in (-1, 2) for m__ in g[m_]):
                        sq(m_, c, 0, 2)

        # everything else is a draw.

        # return state[1,2,m].
        return s[1][2][0]
