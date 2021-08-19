class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 1000000007
        if n == 0:
            return 0
        dp = [[[0] * (max(rollMax) + 2) for _ in range(7)] for __ in range(n + 1)]
        for i in range(1, 7):
            if rollMax[i - 1] > 0:
                dp[1][i][1] = 1
        for x in range(2, n + 1):
            for i in range(1, 7):
                for k in range(1, rollMax[i - 1]):
                    dp[x][i][k + 1] = dp[x - 1][i][k] % MOD
                for j in range(1, 7):
                    if j == i:
                        continue
                    for k in range(1, rollMax[i - 1] + 1):
                        dp[x][j][1] = (dp[x][j][1] + dp[x - 1][i][k]) % MOD
        num = 0
        for i in range(1, 7):
            for k in range(1, max(rollMax) + 1):
                num = (num + dp[n][i][k]) % MOD
        return num
