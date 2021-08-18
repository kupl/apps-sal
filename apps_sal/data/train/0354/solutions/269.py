class Solution:
    def dieSimulator(self, n, rollMax):
        if n == 1:
            return 6
        mod = int(1e9 + 7)
        dp = [[0] * 6 for i in range(n)]
        for j in range(6):
            dp[0][j] = 1
        sums = [0] * n
        sums[0] = 6
        for i in range(1, n):
            for j in range(6):
                invalid = 0
                k = i - rollMax[j]
                if k == 0:
                    invalid = 1
                elif k > 0:
                    invalid = sums[k - 1] - dp[k - 1][j]
                dp[i][j] = ((sums[i - 1] - invalid) % mod + mod) % mod
                sums[i] = (sums[i] + dp[i][j]) % mod
        return sums[-1]
