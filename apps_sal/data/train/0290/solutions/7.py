from itertools import permutations
from functools import lru_cache


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        def bin_search(t, d):
            if t > cuts[-1]:
                return float('inf') if d == '+' else len(cuts) - 1
            if t < cuts[0]:
                return float('-inf') if d == '-' else 0
            (l, r) = (0, len(cuts) - 1)
            while l <= r:
                m = (l + r) // 2
                if cuts[m] > t:
                    r = m - 1
                elif cuts[m] < t:
                    l = m + 1
                else:
                    return m + 1 if d == '+' else m - 1
            return l if d == '+' else r

        @lru_cache(None)
        def helper(st, end):
            l = bin_search(st, '+')
            r = bin_search(end, '-')
            n = max(r - l + 1, 0)
            if n == 1:
                return end - st
            if n == 0:
                return 0
            min_cost = float('inf')
            for i in range(l, r + 1):
                min_cost = min(min_cost, end - st + helper(st, cuts[i]) + helper(cuts[i], end))
            return min_cost
        cuts.sort()
        return helper(0, n)
