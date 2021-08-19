class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 1000000007
        if n == 0:
            return 0
        dict = {}
        dict[1] = [6, 8]
        dict[2] = [7, 9]
        dict[3] = [4, 8]
        dict[4] = [3, 9, 0]
        dict[5] = []
        dict[6] = [1, 7, 0]
        dict[7] = [2, 6]
        dict[8] = [1, 3]
        dict[9] = [2, 4]
        dict[0] = [4, 6]
        dp = [0] * 10
        for i in range(10):
            dp[i] = [0] * (n + 1)
        for i in range(10):
            dp[i][0] = 0
            dp[i][1] = 1
        sum = 0
        for j in range(2, n + 1):
            for i in range(10):
                for k in dict[i]:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1]) % mod
        for i in range(0, 10):
            sum = (sum + dp[i][n]) % mod
        return sum % mod
