class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def min_cost(left_end=0, right_end=n):
            if any(left_end < cut < right_end for cut in cuts):
                cost = right_end - left_end
                nxt_costs = min(
                    min_cost(left_end, cut) + min_cost(cut, right_end)
                    for cut in cuts
                    if left_end < cut < right_end
                )
                return nxt_costs + cost
            return 0

        return min_cost()
