from functools import lru_cache


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache
        def helper(x):
            if x == 1:
                return 1
            if x % 2 == 0:
                return 1 + helper(x // 2)
            return helper(3 * x + 1) + 1
        lookup = {}
        for x in range(lo, hi + 1):
            lookup[x] = helper(x)
        return sorted(lookup.items(), key=lambda x: x[1])[k - 1][0]
