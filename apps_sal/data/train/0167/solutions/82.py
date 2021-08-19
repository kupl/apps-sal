class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[sys.maxsize for i in range(N + 1)] for j in range(K + 1)]

        def DP(k, n):
            if k < 0 or n < 0:
                return 0
            if k == 0:
                return 0
            if k == 1:
                return n
            if n == 0:
                return 0
            if n == 1:
                return 1
            if dp[k][n] != sys.maxsize:
                return dp[k][n]
            l = 0
            r = n
            while l < r:
                m = (l + r) // 2
                if DP(k - 1, m - 1) >= DP(k, n - m):
                    r = m
                else:
                    l = m + 1
            dp[k][n] = 1 + max(DP(k - 1, l - 1), DP(k, n - l))
            return dp[k][n]
        return DP(K, N)
