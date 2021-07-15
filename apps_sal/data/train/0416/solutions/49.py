class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        # dp[t][i][j] := game outcome when at time t, mouse at i, cat at j
        ## 0: draw, 1: mouse wins, 2: cat wins
        dp = [[[-1]*N for _ in range(N)] for m in range(2*N)]
        
        for m in range(2*N):
            for i in range(N):
                dp[m][i][i] = 2 # win by cat
                dp[m][0][i] = 1 # win by mouse
        # dp = 0 when m==2N
        
        def _search(t, x, y):
            # time, mouse pos, cat pos
            if t==2*N: return 0
            if dp[t][x][y]!=-1: return dp[t][x][y]
            
            if t%2==0: # mouse
                winByCat = True
                for i in graph[x]:
                    nxt = _search(t+1, i, y)
                    if nxt==1:
                        dp[t][x][y] = 1
                        return 1
                    if nxt!=2:
                        winByCat = False
                if winByCat:
                    dp[t][x][y] = 2
                    return 2
                else:
                    dp[t][x][y] = 0
                    return 0
            else: # cat
                winByMouse = True
                for i in graph[y]:
                    if i!=0: # cat cannot be at the hole -- 0
                        nxt = _search(t+1, x, i)
                        if nxt==2:
                            dp[t][x][y] = 2
                            return 2
                        if nxt!=1:
                            winByMouse = False
                if winByMouse:
                    dp[t][x][y] = 1
                    return 1
        
        
        return _search(0, 1, 2)
