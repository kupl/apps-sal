class Solution:

    def catMouseGame(self, g):
        mem = [[[-1 for i in range(1 + 2 * len(g))] for i in range(1 + 2 * len(g))] for i in range(2 * len(g))]

        def storeRet(m, c, t, v):
            mem[m][c][t] = v
            return mem[m][c][t]
        (draw, mouseWin, catWin) = (lambda m, c, t: storeRet(m, c, t, 0), lambda m, c, t: storeRet(m, c, t, 1), lambda m, c, t: storeRet(m, c, t, 2))

        def play(m, c, t):
            if mem[m][c][t] != -1:
                return mem[m][c][t]
            if t >= 2 * len(g):
                return 0
            if not t % 2:
                drawFound = False
                for n in g[m]:
                    if n == 0:
                        return mouseWin(m, c, t)
                    if n == c:
                        continue
                    nextTurn = play(n, c, t + 1)
                    if nextTurn == 1:
                        return mouseWin(m, c, t)
                    if nextTurn == 0:
                        drawFound = True
                return draw(m, c, t) if drawFound else catWin(m, c, t)
            else:
                drawFound = False
                for n in g[c]:
                    if n == m:
                        return catWin(m, c, t)
                    if n == 0:
                        continue
                    nextTurn = play(m, n, t + 1)
                    if nextTurn == 2:
                        return catWin(m, c, t)
                    if nextTurn == 0:
                        drawFound = True
                return draw(m, c, t) if drawFound else mouseWin(m, c, t)
        return play(1, 2, 0)
