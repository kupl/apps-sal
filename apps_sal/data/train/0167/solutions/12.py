class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == 0:
                return 0
            if i == 1:
                return j
            if j == 1:
                return 1
            (lo, hi) = (1, j)
            while lo < hi:
                k = lo + (hi - lo) // 2
                if dp(i - 1, k - 1) < dp(i, j - k):
                    lo = k + 1
                else:
                    hi = k
            return 1 + dp(i - 1, lo - 1)
        return dp(K, N)
