class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * 6 for _ in range(16)] for _ in range(n)]
        for k in range(6):
            dp[0][1][k] = 1
        mod = 10 ** 9 + 7
        for i in range(1, n):
            for k in range(6):
                for prev in range(6):
                    for j in range(1, min(rollMax[prev], i + 1) + 1):
                        if prev == k:
                            dp[i][j][k] += dp[i - 1][j - 1][k]
                            dp[i][j][k] %= mod
                        else:
                            dp[i][1][k] += dp[i - 1][j][prev]
                            dp[i][1][k] %= mod
        return sum((dp[n - 1][j][k] for k in range(6) for j in range(1, min(n, rollMax[k]) + 1))) % mod
