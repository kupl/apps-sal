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
