class Solution:
    def catMouseGame(self, g: List[List[int]]) -> int:

        n = len(g)
        s = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        q = deque()

        def sq(m, c, t, v):
            if s[m][c][t] == 0:
                q.append((m, c, t))
                s[m][c][t] = v

        for m in range(n):
            for t in range(2):
                sq(m, 0, t, -1)
        for c in range(n):
            for t in range(2):
                sq(0, c, t, 1)
        for x in range(n):
            for t in range(2):
                sq(x, x, t, 2)

        while q:
            m, c, t = state = q.popleft()
            if t == 1 and s[m][c][t] == 1:
                for m_ in g[m]:
                    sq(m_, c, 0, 1)

            if t == 0 and s[m][c][t] == 2:
                for c_ in g[c]:
                    sq(m, c_, 1, 2)

            if t == 0 and s[m][c][t] == 1:
                for c_ in g[c]:
                    if all(s[m][c__][0] in (-1, 1) for c__ in g[c_]):
                        sq(m, c_, 1, 1)

            if t == 1 and s[m][c][t] == 2:
                for m_ in g[m]:
                    if all(s[m__][c][1] in (-1, 2) for m__ in g[m_]):
                        sq(m_, c, 0, 2)

            if s[1][2][0]:
                return s[1][2][0]

        return 0
