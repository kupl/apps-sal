from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        INF = 10**9

        @lru_cache(None)
        def dp(i, c, k):
            # print(i, c, k, i == m)
            if k > target:
                return INF
            if i >= m:
                return 0 if k == target else INF
            if houses[i] > 0:
                k_next = k if houses[i] == c else k + 1
                return dp(i + 1, houses[i], k_next)

            result = INF
            for j in range(1, n + 1):
                k_next = k if j == c else k + 1
                result = min(result, cost[i][j - 1] + dp(i + 1, j, k_next))

            return result


        ans = dp(0, 0, 0)
        return ans if ans < INF else -1


