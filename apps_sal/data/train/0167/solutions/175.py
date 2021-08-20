class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(k, n):
            ans = 0
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    (l, r) = (1, n)
                    while l + 1 < r:
                        x = (l + r) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)
                        if t1 > t2:
                            r = x
                        elif t1 < t2:
                            l = x
                        else:
                            l = r = x
                    ans = 1 + min((max(dp(k - 1, x - 1), dp(k, n - x)) for x in (l, r)))
                memo[k, n] = ans
            return memo[k, n]
        return dp(K, N)
