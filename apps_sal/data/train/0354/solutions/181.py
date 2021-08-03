class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(len(rollMax) + 1)] for _ in range(n + 1)]
        for j in range(len(rollMax)):
            dp[1][j] = 1
            dp[1][-1] += dp[1][j]
        for i in range(2, n + 1):
            for j in range(len(rollMax)):
                dp[i][j] = dp[i - 1][-1]
                k = i - rollMax[j]
                if k == 1:
                    dp[i][j] -= 1
                elif k > 1:
                    dp[i][j] -= (dp[k - 1][-1] - dp[k - 1][j])
                dp[i][-1] += dp[i][j]
        return dp[-1][-1] % int(1e9 + 7)
