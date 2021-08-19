class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for i in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                if i == 0:
                    if j % coins[i] == 0:
                        dp[i][j] = j // coins[i]
                    else:
                        dp[i][j] = float('inf')
                elif j - coins[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                elif j == coins[i]:
                    dp[i][j] = 1
                elif j > coins[i]:
                    dp[i][j] = min(1 + dp[i][j - coins[i]], dp[i - 1][j])
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
