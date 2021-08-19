class Solution:
    def catMouseGame(self, graph):
        mem = [[[-1 for i in range(1 + 2 * len(graph))] for i in range(1 + 2 * len(graph))] for i in range(2 * len(graph))]

        def storeRet(mouse, cat, turn, value):
            mem[mouse][cat][turn] = value
            return mem[mouse][cat][turn]

        def play(mouse, cat, turn):
            #print(f'turn {turn} mouse {mouse} cat {cat}')
            if mem[mouse][cat][turn] != -1:
                #print(f'{mouse} {cat} {turn} already calc: {mem[mouse][cat][turn]}')
                return mem[mouse][cat][turn]
            if turn >= len(graph) * 2:
                return 0
            if turn % 2:
                #print('mouse turn')
                ans = 2
                for node in graph[mouse]:
                    #print(f'mouse check {node}')
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
                #print('cat turn')
                ans = 1
                for node in graph[cat]:
                    #print(f'cat check {node}')
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
        return play(1, 2, 1)
