class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf') for _ in range(n)] for _ in range(target + 1)] for _ in range(m)]
        for c in range(1, n + 1):
            if houses[0] == 0:
                dp[0][1][c - 1] = cost[0][c - 1]
            elif houses[0] == c:
                dp[0][1][c - 1] = 0
        for i in range(1, m):
            for k in range(1, min(i + 1, target) + 1):
                for c in range(1, n + 1):
                    prev = min(dp[i - 1][k][c - 1], min([dp[i - 1][k - 1][c_ - 1] for c_ in range(1, n + 1) if c_ != c]))
                    if houses[i] == 0 or houses[i] == c:
                        dp[i][k][c - 1] = prev + cost[i][c - 1] * (houses[i] == 0)
        res = min(dp[-1][-1])
        return -1 if res == float('inf') else res
