class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def DP(k, n):
            if (k, n) not in memo:
                if n == 0:
                    res = 0
                elif k == 1:
                    res = n
                else:
                    l, r = 1, n
                    while l < r:
                        mid = (l + r) // 2
                        t1 = DP(k - 1, mid - 1)
                        t2 = DP(k, n - mid)

                        if t1 < t2:
                            l = mid + 1
                        else:
                            r = mid

                    res = 1 + max(DP(k - 1, l - 1), DP(k, n - l))
                memo[k, n] = res
            return memo[k, n]

        return DP(K, N)
