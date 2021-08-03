class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(idx, prev_color, k):
            if idx >= m:
                return 0 - int(k != 0)
            if k < 0:
                return -1

            if houses[idx] != 0:
                return dp(idx + 1, houses[idx], k - int(prev_color != houses[idx]))

            best = math.inf

            for new_color in range(1, n + 1):
                new_cost = cost[idx][new_color - 1]
                other_cost = dp(idx + 1, new_color, k - int(new_color != prev_color))

                if other_cost >= 0:
                    best = min(best, new_cost + other_cost)

            return best if best is not math.inf else -1
        res = dp(0, 0, target)
        return res if res != math.inf else -1
