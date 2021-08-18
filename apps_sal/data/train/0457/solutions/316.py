class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount + 1)] for i in range(len(coins))]
        col = amount + 1
        for i in range(len(coins)):
            for j in range(1, col):
                if i == 0:
                    r = i
                    c = j - coins[i]
                    if c < 0 or dp[r][c] == -1:
                        dp[i][j] = -1
                    else:
                        dp[i][j] = dp[r][c] + 1
                else:
                    incIndex = j - coins[i]
                    if incIndex < 0 or dp[i][incIndex] == -1:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][incIndex] + 1
                        if dp[i - 1][j] != -1:
                            dp[i][j] = min(dp[i - 1][j], dp[i][incIndex] + 1)
        return dp[len(coins) - 1][col - 1]
