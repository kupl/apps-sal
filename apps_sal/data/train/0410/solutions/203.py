class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache(None)
        def p(x):
            if x == 1:
                return 0
            elif x & 1:
                return p(3 * x + 1) + 1
            else:
                return p(x >> 1) + 1
        return sorted(range(lo, hi + 1), key=p)[k - 1]
