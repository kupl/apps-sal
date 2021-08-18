class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = []
        for i in range(m):
            dp.append([[-1] * (n + 1) for _ in range(m + 1)])
        for i in range(m):
            for j in range(1, i + 2):
                for k in range(1, n + 1):
                    if i == 0:
                        if houses[0] == 0:
                            dp[0][1][k] = cost[0][k - 1]
                        elif houses[0] == k:
                            dp[0][1][k] = 0
                    else:
                        if houses[i] == 0:
                            options = []
                            for last_color in range(1, n + 1):
                                if last_color == k:
                                    if dp[i - 1][j][k] != -1:
                                        options.append(cost[i][k - 1] + dp[i - 1][j][k])
                                else:
                                    if dp[i - 1][j - 1][last_color] != -1:
                                        options.append(cost[i][k - 1] + dp[i - 1][j - 1][last_color])
                            if len(options) != 0:
                                dp[i][j][k] = min(options)
                        elif houses[i] == k:
                            options = []
                            for last_color in range(1, n + 1):
                                if last_color == k:
                                    if dp[i - 1][j][k] != -1:
                                        options.append(dp[i - 1][j][k])
                                else:
                                    if dp[i - 1][j - 1][last_color] != -1:
                                        options.append(dp[i - 1][j - 1][last_color])
                            if len(options) != 0:
                                dp[i][j][k] = min(options)
        costs = list([x for x in dp[m - 1][target] if x != -1])
        if len(costs) == 0:
            return -1
        else:
            return min(costs)
