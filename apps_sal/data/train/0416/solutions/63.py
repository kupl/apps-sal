class Solution:
    def catMouseGame(self, g):
        mem = [[[-1 for i in range(1 + 2 * len(g))] for i in range(1 + 2 * len(g))] for i in range(2 * len(g))]

        def storeRet(m, c, t, v):
            mem[m][c][t] = v
            return mem[m][c][t]
        HOLE, DRAW, MOUSE_WIN, CAT_WIN = 0, 0, 1, 2
        draw, mouseWin, catWin = lambda m, c, t: storeRet(m, c, t, DRAW), lambda m, c, t: storeRet(m, c, t, MOUSE_WIN), lambda m, c, t: storeRet(m, c, t, CAT_WIN)

        def play(m, c, t):
            if mem[m][c][t] != -1:
                return mem[m][c][t]  # return cached
            if t >= 2 * len(g):
                return 0  # repeated states
            if not t % 2:  # mouse turn
                drawFound = False
                for n in g[m]:
                    if n == HOLE:
                        return mouseWin(m, c, t)
                    if n == c:
                        continue
                    nextTurn = play(n, c, t + 1)
                    if nextTurn == MOUSE_WIN:
                        return mouseWin(m, c, t)
                    if nextTurn == DRAW:
                        drawFound = True
                return draw(m, c, t) if drawFound else catWin(m, c, t)
            else:  # cat turn
                drawFound = False
                for n in g[c]:
                    if n == m:
                        return catWin(m, c, t)
                    if n == HOLE:
                        continue
                    nextTurn = play(m, n, t + 1)
                    if nextTurn == CAT_WIN:
                        return catWin(m, c, t)
                    if nextTurn == DRAW:
                        drawFound = True
                return draw(m, c, t) if drawFound else mouseWin(m, c, t)
        return play(1, 2, 0)
