class Solution:
    def catMouseGame(self, graph):
        mem = [[[-1 for i in range(1+2*len(graph))] for i in range(1+2*len(graph))] for i in range(2*len(graph))]
        def storeRet(mouse,cat,turn,value):
            mem[mouse][cat][turn] = value
            return mem[mouse][cat][turn]
        mouseWin = lambda m,c,t:storeRet(m,c,t,1)
        catWin = lambda m,c,t:storeRet(m,c,t,2)
        def play(mouse, cat, turn):
            if mem[mouse][cat][turn]!=-1: return mem[mouse][cat][turn]
            if turn >= len(graph)*2: return 0
            if not turn % 2:
                ans = 2
                for node in graph[mouse]:
                    if node == 0: return mouseWin(mouse,cat,turn)
                    if node == cat: continue
                    res = play(node, cat, turn+1)
                    if res == 1: return mouseWin(mouse,cat,turn)
                    if res == 0: ans = 0
                return storeRet(mouse,cat,turn,ans)
            else:
                ans = 1
                for node in graph[cat]:
                    if node == mouse: return catWin(mouse,cat,turn)
                    if node == 0: continue
                    res = play(mouse, node, turn+1)
                    if res == 2: return catWin(mouse,cat,turn)
                    if res == 0: ans = 0
                return storeRet(mouse,cat,turn,ans)
        return play(1,2,0)
