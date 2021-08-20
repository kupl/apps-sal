class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache
        def getPower(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + getPower(x // 2)
            return 1 + getPower(3 * x + 1)
        return sorted([(getPower(x), x) for x in range(lo, hi + 1)])[k - 1][1]
