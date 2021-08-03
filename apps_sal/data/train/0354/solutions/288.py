class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n)]
        prev = defaultdict(int)
        MOD = 10**9 + 7

        for i in range(6):
            dp[0][i] = 1
            prev[(i, 1)] = 1

        for i in range(1, n):
            new = defaultdict(int)
            for j in range(6):
                new[(j, 1)] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] - dp[i - 1][j]
                dp[i][j] += new[(j, 1)]

                for k in range(1, rollMax[j]):
                    new[(j, k + 1)] = prev[(j, k)]
                    dp[i][j] += new[(j, k + 1)]
                dp[i][j] %= MOD
            prev = new

        return sum(dp[-1]) % MOD
