class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(10)] for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        def check(k):
            if k == 0:
                return [4, 6]
            elif k == 1:
                return [6, 8]
            elif k == 2:
                return [7, 9]
            elif k == 3:
                return [4, 8]
            elif k == 4:
                return [0, 3, 9]
            elif k == 5:
                return []
            elif k == 6:
                return [0, 1, 7]
            elif k == 7:
                return [2, 6]
            elif k == 8:
                return [1, 3]
            else:
                return [2, 4]
        for i in range(1, n):
            for j in range(10):
                for k in check(j):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod
        ans = 0
        for i in range(10):
            ans = (ans + dp[n - 1][i]) % mod
        return ans
