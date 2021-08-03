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

#         @lru_cache(None)
#         def dp(idx: int, prev_color: int, k: int) -> int:

#             # No more houses left to paint, return true if there are no more neighborhoods
#             # to paint, false otherwise
#             if idx >= m:
#                 return 0 - int(k != 0)

#             # No more neighborhoods colors available
#             if k < 0:
#                 return -1

#             # Check if this house is already painted, if so, go to the next house
#             # Note: `k - int(prev_color != new_color)` decreases the number of
#             # neighborhoods left to paint if the current house color is different than the
#             # previous one
#             if houses[idx] != 0:
#                 return dp(idx + 1, houses[idx], k - int(prev_color != houses[idx]))

#             # Decide on the best color to paint current house
#             best = -1

#             # Try all possible colors
#             for new_color in range(1, n + 1):
#                 new_color_cost = cost[idx][new_color - 1]
#                 other_costs = dp(idx + 1, new_color, k - int(prev_color != new_color))

#                 # Check if painting this house with `new_color` will give us a lower cost
#                 if other_costs >= 0:
#                     best = min(best if best > 0 else float(\"inf\"),
#                                new_color_cost + other_costs)
#             return best

#         # Start with the first house
#         return dp(0, 0, target)
