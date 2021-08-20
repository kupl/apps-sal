class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        self.dp = [[[-1] * n for _ in range(n)] for _ in range(2 * n)]

        def helper(t, x, y):
            if t == 2 * n:
                return 0
            if x == y:
                self.dp[t][x][y] = 2
                return 2
            if x == 0:
                self.dp[t][x][y] = 1
                return 1
            if self.dp[t][x][y] != -1:
                return self.dp[t][x][y]
            mouseTurn = t % 2 == 0
            if mouseTurn:
                catWins = True
                for nei in graph[x]:
                    tmp = helper(t + 1, nei, y)
                    if tmp == 1:
                        self.dp[t][x][y] = 1
                        return 1
                    if tmp != 2:
                        catWins = False
                if catWins:
                    self.dp[t][x][y] = 2
                    return 2
                else:
                    self.dp[t][x][y] = 0
                    return 0
            else:
                mouseWins = True
                for nei in graph[y]:
                    if nei == 0:
                        continue
                    tmp = helper(t + 1, x, nei)
                    if tmp == 2:
                        self.dp[t][x][y] = 2
                        return 2
                    if tmp != 1:
                        mouseWins = False
                if mouseWins:
                    self.dp[t][x][y] = 1
                    return 1
                else:
                    self.dp[t][x][y] = 0
                    return 0
            return self.dp[t][x][y]
        return helper(0, 1, 2)
