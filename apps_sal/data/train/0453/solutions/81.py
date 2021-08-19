class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
        if houses[0] != 0:
            dp[houses[0]][1] = 0
        else:
            for c in range(n):
                dp[c + 1][1] = cost[0][c]
        for i in range(1, len(houses)):
            tmp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
            for j in range(1, target + 1):
                if houses[i] != 0:
                    if houses[i - 1] == 0:
                        tmp[houses[i]][j] = min(dp[houses[i]][j], min([dp[color + 1][j - 1] for color in range(n) if color + 1 != houses[i]]))
                    elif houses[i - 1] == houses[i]:
                        tmp[houses[i]][j] = dp[houses[i]][j]
                    else:
                        tmp[houses[i]][j] = dp[houses[i - 1]][j - 1]
                elif houses[i - 1]:
                    for c in range(n):
                        if c + 1 == houses[i - 1]:
                            tmp[c + 1][j] = dp[c + 1][j] + cost[i][c]
                        else:
                            tmp[c + 1][j] = dp[houses[i - 1]][j - 1] + cost[i][c]
                else:
                    for c in range(n):
                        tmp[c + 1][j] = min(dp[c + 1][j], min([dp[color + 1][j - 1] for color in range(n) if color != c])) + cost[i][c]
            dp = tmp
        res = min([dp[c + 1][target] for c in range(n)])
        return res if res != float('inf') else -1
