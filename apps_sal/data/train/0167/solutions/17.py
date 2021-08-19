class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def dp(k, n):
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                lo, hi = 1, n
                # keep a gap of 2 X values to manually check later
                while lo < hi:
                    x = (lo + hi) // 2
                    t1 = dp(k - 1, x - 1)
                    t2 = dp(k, n - x)

                    if t1 < t2:
                        lo = x + 1
                    else:
                        hi = x
                ans = 1 + max(dp(k - 1, lo - 1), dp(k, n - lo))
            return ans
        return dp(K, N)
