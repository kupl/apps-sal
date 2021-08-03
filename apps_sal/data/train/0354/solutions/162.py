class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j][k] : ith roll, end with j with consecutive k times
        MOD = 10 ** 9 + 7
        rdim = max(rollMax)
        dp = [[[0] * rdim for _ in range(6)] for _ in range(n)]

        # init
        for j in range(6):
            dp[0][j][0] = 1

        for i in range(1, n):
            for j in range(6):
                for prev in range(6):
                    for k in range(min(rollMax[prev], i + 1)):
                        if j == prev and k < rollMax[prev] - 1:
                            dp[i][j][k + 1] += dp[i - 1][prev][k] % MOD
                        if j != prev:
                            dp[i][j][0] += dp[i - 1][prev][k] % MOD

        return sum(dp[n - 1][j][k] for j in range(6) for k in range(rdim)) % MOD
