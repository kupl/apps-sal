class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[math.inf for _ in range(amount + 1)] for _ in range(n)]

        for i, coin in enumerate(coins):
            for t in range(amount + 1):
                if t == 0:
                    dp[i][t] = 0
                if i > 0:
                    dp[i][t] = dp[i - 1][t]

                if t >= coin:
                    dp[i][t] = min(dp[i][t], dp[i][t - coin] + 1)
        return -1 if dp[n - 1][amount] == math.inf else dp[n - 1][amount]
