class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        for n in range(1, N + 1):
            dp[1][n] = n
        for k in range(2, K + 1):
            dp[k][1] = 1
        # dp[k][n] <= n
        for k in range(2, K + 1):
            m = 1
            for n in range(2, N + 1):
                while m < n and dp[k - 1][m - 1] < dp[k][n - m]:
                    m += 1
                # dp[k][n] = min(max(dp[k - 1][m - 1], dp[k][n - m]) + 1 for m in range(1, n + 1))
                # l, r = 1, n
                # while l < r:
                #     m = (l + r) >> 1
                #     a, b = dp[k - 1][m - 1], dp[k][n - m]
                #     if a > b:
                #         r = m
                #     elif b > a:
                #         l = m + 1
                #     else:
                #         break
                dp[k][n] = max(dp[k - 1][m - 1], dp[k][n - m]) + 1
        # for _ in dp:
        #     print(_)
        return dp[-1][-1]
