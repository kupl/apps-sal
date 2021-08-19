class Solution(object):

    def superEggDrop(self, K, N):
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0 or n == 1:
                    ans = n
                elif k == 1:
                    ans = n
                else:
                    (lo, hi) = (1, n)
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)
                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    ans = 1000000
                    for x in range(lo, hi + 1):
                        temp = 1 + max(dp(k - 1, x - 1), dp(k, n - x))
                        if ans > temp:
                            ans = temp
                memo[k, n] = ans
            return memo[k, n]
        return dp(K, N)
