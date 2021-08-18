class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(idx: int, pc: int, k: int) -> int:
            if idx >= m:
                return 0 - int(k != 0)
            if k < 0:
                return -1
            if houses[idx] != 0:
                return dp(idx + 1, houses[idx], k - int(pc != houses[idx]))

            ans = -1
            for i in range(1, n + 1):
                new_cost = cost[idx][i - 1]
                prev_cost = dp(idx + 1, i, k - int(pc != i))
                if prev_cost >= 0:
                    ans = min(ans if ans > 0 else float('inf'), new_cost + prev_cost)

            return ans

        return dp(0, 0, target)
