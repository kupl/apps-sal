class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 7 for _ in range(n + 1)]
        dp[0][6] = 1
        for i in range(6):
            dp[1][i] = 1
        dp[1][6] = 6
        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, min(rollMax[j], i) + 1):
                    dp[i][j] += dp[i - k][6] - dp[i - k][j]
                    dp[i][j] %= mod
            dp[i][6] = sum([dp[i][j] for j in range(6)])
            dp[i][6] %= mod
        return dp[n][6]
