from itertools import permutations
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def helper(st, end):
            curr_cuts = [c for c in cuts if st < c < end]
            n = len(curr_cuts)
            if n == 1:
                return end - st
            if n == 0:
                return 0

            min_cost = float('inf')
            for cut in curr_cuts:
                min_cost = min(min_cost, end - st + helper(st, cut) + helper(cut, end))

            return min_cost

        cuts.sort()
        return helper(0, n)
