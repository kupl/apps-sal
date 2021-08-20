class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:

        def search(t, x, y):
            if t == len(graph) * 2:
                return 0
            if x == y:
                dp[t][x][y] = 2
                return 2
            if x == 0:
                dp[t][x][y] = 1
                return 1
            if dp[t][x][y] != -1:
                return dp[t][x][y]
            if t % 2 == 0:
                flag = True
                for i in range(len(graph[x])):
                    nxt = search(t + 1, graph[x][i], y)
                    if nxt == 1:
                        dp[t][x][y] = 1
                        return 1
                    elif nxt != 2:
                        flag = False
                if flag:
                    dp[t][x][y] = 2
                    return 2
                dp[t][x][y] = 0
                return 0
            else:
                flag = True
                for i in range(len(graph[y])):
                    if graph[y][i] != 0:
                        nxt = search(t + 1, x, graph[y][i])
                        if nxt == 2:
                            dp[t][x][y] = 2
                            return 2
                        elif nxt != 1:
                            flag = False
                if flag:
                    dp[t][x][y] = 1
                    return 1
                else:
                    dp[t][x][y] = 0
                    return 0
        n = len(graph)
        dp = [[[-1 for k in range(n)] for j in range(n)] for i in range(2 * n)]
        return search(0, 1, 2)
