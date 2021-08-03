from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache
        def power(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return 1 + power(n // 2)
            else:
                return 1 + power(3 * n + 1)

        powers = [(power(n), n) for n in range(lo, hi + 1)]
        powers.sort()

        return powers[k - 1][1]
