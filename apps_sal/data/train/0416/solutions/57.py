class Solution:

    def catMouseGame(self, graph):
        mem = [[[-1 for i in range(1 + 2 * len(graph))] for i in range(1 + 2 * len(graph))] for i in range(2 * len(graph))]

        def storeRet(mouse, cat, turn, value):
            mem[mouse][cat][turn] = value
            return mem[mouse][cat][turn]

        def mouseWin(m, c, t):
            return storeRet(m, c, t, 1)

        def catWin(m, c, t):
            return storeRet(m, c, t, 2)

        def draw(m, c, t):
            return storeRet(m, c, t, 0)

        def play(mouse, cat, turn):
            if mem[mouse][cat][turn] != -1:
                return mem[mouse][cat][turn]
            if turn >= len(graph) * 2:
                return 0
            if not turn % 2:
                drawFound = False
                for node in graph[mouse]:
                    if node == 0:
                        return mouseWin(mouse, cat, turn)
                    if node == cat:
                        continue
                    res = play(node, cat, turn + 1)
                    if res == 1:
                        return mouseWin(mouse, cat, turn)
                    if res == 0:
                        drawFound = True
                return draw(mouse, cat, turn) if drawFound else catWin(mouse, cat, turn)
            else:
                drawFound = False
                for node in graph[cat]:
                    if node == mouse:
                        return catWin(mouse, cat, turn)
                    if node == 0:
                        continue
                    res = play(mouse, node, turn + 1)
                    if res == 2:
                        return catWin(mouse, cat, turn)
                    if res == 0:
                        drawFound = True
                return draw(mouse, cat, turn) if drawFound else mouseWin(mouse, cat, turn)
        return play(1, 2, 0)
