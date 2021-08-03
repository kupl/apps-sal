import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 0
                if i == 0:
                    dp[i][j] = sys.maxsize - 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[-1][-1] == sys.maxsize - 1:
            return -1
        else:
            return dp[-1][-1]
