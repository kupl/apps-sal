class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, prev, count):
            if count > target:
                return float('inf')
            if i == m:
                return 0 if count == target else float('inf')

            return min((cost[i][c - 1] if c != houses[i] else 0) + dp(i + 1, c, count + (prev != c)) for c in range(1, n + 1) if not houses[i] or c == houses[i])
        ans = dp(0, houses[0], 1 if houses[0] else 0)
        return -1 if ans == float('inf') else ans
