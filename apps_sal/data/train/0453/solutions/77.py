from functools import lru_cache


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(g, i, c):
            if g > target:
                return sys.maxsize
            if i == m:
                return 0 if g == target else sys.maxsize
            ans = sys.maxsize
            if houses[i] != 0:
                ans = min(ans, dp(g + (houses[i] != c), i + 1, houses[i]))
            else:
                for j in range(n):
                    ans = min(ans, cost[i][j] + dp(g + (j + 1 != c), i + 1, j + 1))
            return ans
        ans = dp(0, 0, 0)
        return -1 if ans >= sys.maxsize else ans
