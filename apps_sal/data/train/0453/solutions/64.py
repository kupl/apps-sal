class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        dp = [[[math.inf for k in range(n)] for j in range(target)] for i in range(m)]
        if houses[0]:
            dp[0][0][houses[0] - 1] = 0
        else:
            for k in range(n):
                dp[0][0][k] = cost[0][k]

        pre = houses[0]
        min_neighborhoods = 1
        for i in range(1, m):
            if houses[i]:
                if pre and houses[i] != pre:
                    min_neighborhoods += 1
                pre = houses[i]
            for j in range(min_neighborhoods - 1, min(i + 1, target)):
                for k in (houses[i] - 1,) if houses[i] else range(n):
                    dp[i][j][k] = min(min(dp[i - 1][j - 1][p] for p in range(n) if p != k), dp[i - 1][j][k])
                    if not houses[i]:
                        dp[i][j][k] += cost[i][k]

        ans = min(dp[-1][-1])
        return -1 if ans == math.inf else ans
