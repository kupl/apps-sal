class Solution:
    def catMouseGame(self, g):
        mem = [[[-1 for i in range(1 + 2 * len(g))] for i in range(1 + 2 * len(g))] for i in range(2 * len(g))]

        def storeRet(m, c, t, v):
            mem[m][c][t] = v
            return mem[m][c][t]

        def mouseWin(m, c, t): return storeRet(m, c, t, 1)
        def catWin(m, c, t): return storeRet(m, c, t, 2)
        def draw(m, c, t): return storeRet(m, c, t, 0)

        def play(m, c, t):
            if mem[m][c][t] != -1:
                return mem[m][c][t]
            if t >= len(g) * 2:
                return 0
            if not t % 2:
                drawFound = False
                for n in g[m]:
                    if n == 0:
                        return mouseWin(m, c, t)
                    if n == c:
                        continue
                    res = play(n, c, t + 1)
                    if res == 1:
                        return mouseWin(m, c, t)
                    if res == 0:
                        drawFound = True
                return draw(m, c, t) if drawFound else catWin(m, c, t)
            else:
                drawFound = False
                for n in g[c]:
                    if n == m:
                        return catWin(m, c, t)
                    if n == 0:
                        continue
                    res = play(m, n, t + 1)
                    if res == 2:
                        return catWin(m, c, t)
                    if res == 0:
                        drawFound = True
                return draw(m, c, t) if drawFound else mouseWin(m, c, t)
        return play(1, 2, 0)
