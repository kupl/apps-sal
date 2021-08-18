from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            l, r = 1, n + 1
            while l < r:
                m = l + (r - l) // 2
                if dp(k - 1, m - 1) >= dp(k, n - m):
                    r = m
                else:
                    l = m + 1
            return 1 + max(dp(k - 1, l - 1), dp(k, n - l))

        return dp(K, N)
