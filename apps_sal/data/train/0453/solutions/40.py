class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(i, g, p):
            if i == m:
                return 0 if g == 0 else float('inf')
            if m - i < g:
                return float('inf')
            if houses[i]:
                return dp(i + 1, g - (p != houses[i]), houses[i])
            else:
                return min(dp(i + 1, g - (p != nc), nc) + cost[i][nc - 1] for nc in range(1, n + 1))

        ret = dp(0, target, -1)
        return ret if ret != float('inf') else -1


#         dp = [[[float('inf') for _ in range(target + 1)] for _ in range(1 + n)] for _ in range(m)]
#         if houses[0] != 0:
#             dp[0][houses[0]][1] = 0
#         else:
#             for i in range(1, n + 1):
#                 dp[0][i][1] = cost[0][i - 1]

#         for house in range(1, m):
#             if houses[house] > 0:
#                 for neigh in range(1, target + 1):
#                     c1= houses[house]
#                     dp[house][c1][neigh] = min(min(dp[house - 1][c2][neigh - 1] for c2 in range(1, n + 1) if c2 != c1), dp[house - 1][c1][neigh])
#                 continue
#             for c1 in range(1, n + 1):
#                 for neigh in range(1, target + 1):
#                     for c2 in range(1, n + 1):
#                         if c1 == c2:
#                             dp[house][c1][neigh] = min(dp[house][c1][neigh], dp[house - 1][c2][neigh] + cost[house][c1 - 1])
#                         else:
#                             dp[house][c1][neigh] = min(dp[house][c1][neigh], dp[house - 1][c2][neigh - 1] + cost[house][c1 - 1])
#         ans = min(k[target] for k in dp[-1])
#         return ans if ans != float('inf') else -1
