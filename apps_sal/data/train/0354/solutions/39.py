class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for i in range(n + 1)]
        dp[0][-1] = 1
        for j in range(6):
            dp[1][j] = 1
        dp[1][-1] = 6
        for i in range(2, n + 1):
            for j in range(6):
                dp[i][j] = dp[i - 1][-1]
                k = i - rollMax[j] - 1
                if k >= 0:
                    dp[i][j] -= (dp[k][-1] - dp[k][j])
                dp[i][-1] += dp[i][j]
        return dp[-1][-1] % int(1e9 + 7)
