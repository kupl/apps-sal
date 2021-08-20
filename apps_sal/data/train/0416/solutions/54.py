class Solution:

    def catMouseGame(self, graph):
        mem = [[[-1 for i in range(1 + 2 * len(graph))] for i in range(1 + 2 * len(graph))] for i in range(2 * len(graph))]

        def storeRet(mouse, cat, turn, value):
            mem[mouse][cat][turn] = value
            return mem[mouse][cat][turn]

        def play(mouse, cat, turn):
            if mem[mouse][cat][turn] != -1:
                return mem[mouse][cat][turn]
            if turn >= len(graph) * 2:
                return 0
            if not turn % 2:
                ans = 2
                for node in graph[mouse]:
                    if node == cat:
                        continue
                    if node == 0:
                        return storeRet(mouse, cat, turn, 1)
                    res = play(node, cat, turn + 1)
                    if res == 1:
                        return storeRet(mouse, cat, turn, 1)
                    if res == 0:
                        ans = 0
                return storeRet(mouse, cat, turn, ans)
            else:
                ans = 1
                for node in graph[cat]:
                    if node == 0:
                        continue
                    if node == mouse:
                        return storeRet(mouse, cat, turn, 2)
                    res = play(mouse, node, turn + 1)
                    if res == 2:
                        return storeRet(mouse, cat, turn, 2)
                    if res == 0:
                        ans = 0
                return storeRet(mouse, cat, turn, ans)
        return play(1, 2, 0)
