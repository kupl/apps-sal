class Solution:
    def catMouseGame(self, g: List[List[int]]) -> int:

        MTURN, CTURN = 0, 1
        ILLEGAL, UNKNOWN, MWIN, CWIN = -1, 0, 1, 2

        n = len(g)
        s = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        q = deque()

        def sq(m, c, t, v):
            if s[m][c][t] == UNKNOWN:
                q.append((m, c, t))
                s[m][c][t] = v

        for t in (MTURN, CTURN):
            for x in range(n):
                sq(x, 0, t, ILLEGAL)
                sq(0, x, t, MWIN)
                sq(x, x, t, CWIN)

        while q:
            m, c, t = q.popleft()

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

            if s[1][2][MTURN]:
                return s[1][2][MTURN]

        return 0
