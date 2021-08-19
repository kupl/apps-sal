class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(n, k):
            if (n, k) not in memo:
                if n == 0:
                    ret = 0
                elif k == 1:
                    ret = n
                else:
                    (lo, hi) = (1, n)
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(n - x, k)
                        t2 = dp(x - 1, k - 1)
                        if t1 < t2:
                            hi = x
                        elif t1 > t2:
                            lo = x
                        else:
                            lo = hi = x
                    ret = 1 + min((max(dp(n - x, k), dp(x - 1, k - 1)) for x in (lo, hi)))
                memo[n, k] = ret
            return memo[n, k]
        return dp(N, K)
