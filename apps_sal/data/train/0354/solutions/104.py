class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n)]
        for j in range(6):
            dp[0][j] = 1
        dp[0][-1] = 6

        for i in range(1, n):
            total = 0
            for j in range(6):
                dp[i][j] = dp[i - 1][-1]
                if i - rollMax[j] == 0:
                    dp[i][j] -= 1
                if i - rollMax[j] >= 1:
                    dp[i][j] -= dp[i - rollMax[j] - 1][-1] - dp[i - rollMax[j] - 1][j]
                total += dp[i][j]
            dp[i][-1] = total

        return dp[-1][-1] % (10 ** 9 + 7)
