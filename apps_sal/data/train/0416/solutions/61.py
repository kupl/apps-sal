class Solution:
    def catMouseGame(self, graph):
        mem = [[[-1 for i in range(1+2*len(graph))] for i in range(1+2*len(graph))] for i in range(2*len(graph))]
        def storeRet(m,c,t,v):
            mem[m][c][t] = v
            return mem[m][c][t]
        mouseWin = lambda m,c,t:storeRet(m,c,t,1)
        catWin = lambda m,c,t:storeRet(m,c,t,2)
        draw = lambda m,c,t:storeRet(m,c,t,0)
        
        def play(m, c, t):
            if mem[m][c][t]!=-1: return mem[m][c][t] # already visited this game state
            if t >= len(graph)*2: return 0 # repeated states
            if not t % 2: # mouse turn
                drawFound = False
                for n in graph[m]:
                    if n == 0: return mouseWin(m,c,t)
                    if n == c: continue
                    res = play(n, c, t+1)
                    if res == 1: return mouseWin(m,c,t)
                    if res == 0: drawFound = True
                return draw(m,c,t) if drawFound else catWin(m,c,t)
            else: # cat turn
                drawFound=False
                for n in graph[c]:
                    if n == m: return catWin(m,c,t)
                    if n == 0: continue
                    res = play(m, n, t+1)
                    if res == 2: return catWin(m,c,t)
                    if res == 0: drawFound = True
                return draw(m,c,t) if drawFound else mouseWin(m,c,t)
        return play(1,2,0)
