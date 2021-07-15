class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j][k]: number of sequences end with k js when throw dice for i times
        # dp[i][*][1] = 1
        # dp[i][j][1] = sum(dp[i - 1][p][*]) j != p
        # dp[i][j][k + 1] = dp[i - 1][j][k] k < rollMax[j]
        mod = 10**9 + 7
        maxRoll = max(rollMax)
        dp = [[[0] * (maxRoll + 1) for _ in range(6)] for _ in range(n + 1)]
        for j in range(6):
            dp[1][j][1] = 1
        for i in range(2, n + 1):
            for j in range(6):
                for p in range(6):
                    for k in range(1, rollMax[p] + 1):
                        if p != j:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][p][k]) % mod
                        elif k < rollMax[p]:
                            dp[i][j][k + 1] = dp[i - 1][j][k]
        res = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                res = (res + dp[n][j][k]) % mod
        return res
