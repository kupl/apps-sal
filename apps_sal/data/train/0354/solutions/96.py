class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * (len(rollMax) + 1) for _ in range(n + 1)]
        for idx in range(len(rollMax)):
            dp[1][idx] = 1
            dp[1][-1] += dp[1][idx]
        for row in range(2, n + 1):
            for col in range(len(rollMax)):
                dp[row][col] = dp[row - 1][-1]
                delta = row - rollMax[col]
                if delta == 1:
                    dp[row][col] -= 1
                elif delta > 1:
                    dp[row][col] -= dp[delta - 1][-1] - dp[delta - 1][col]
                dp[row][-1] += dp[row][col]
        return dp[n][len(rollMax)] % (pow(10, 9) + 7)
