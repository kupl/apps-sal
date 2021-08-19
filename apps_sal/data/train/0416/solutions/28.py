class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        dp = [[[-1] * N for _ in range(N)] for m in range(2 * N)]
        for m in range(2 * N):
            for i in range(N):
                dp[m][i][i] = 2
                dp[m][0][i] = 1

        def _search(t, x, y):
            if t == 2 * N:
                return 0
            if dp[t][x][y] != -1:
                return dp[t][x][y]
            if t % 2 == 0:
                winByCat = True
                for i in graph[x]:
                    nxt = _search(t + 1, i, y)
                    if nxt == 1:
                        dp[t][x][y] = 1
                        return 1
                    if nxt != 2:
                        winByCat = False
                if winByCat:
                    dp[t][x][y] = 2
                    return 2
                else:
                    dp[t][x][y] = 0
                    return 0
            else:
                winByMouse = True
                for i in graph[y]:
                    if i != 0:
                        nxt = _search(t + 1, x, i)
                        if nxt == 2:
                            dp[t][x][y] = 2
                            return 2
                        if nxt != 1:
                            winByMouse = False
                if winByMouse:
                    dp[t][x][y] = 1
                    return 1
                else:
                    dp[t][x][y] = 0
                    return 0
        return _search(0, 1, 2)
