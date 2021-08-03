class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        dp[0][6] = 1
        for i in range(6):
            dp[1][i] = 1
        dp[1][6] = 6
        for i in range(2, n + 1):
            for roll in range(6):
                for j in range(1, rollMax[roll] + 1):
                    if i - j < 0:
                        break
                    dp[i][roll] += dp[i - j][6] - dp[i - j][roll]
                dp[i][6] += dp[i][roll]
        return dp[n][6] % (int(1e9) + 7)
