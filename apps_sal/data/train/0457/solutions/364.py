class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[math.inf for _ in range(amount + 1)] for _ in range(n)]

        for i, coin in enumerate(coins):
            for t in range(amount + 1):
                # * populate the amount=0 columns, as we don't need any coin to make zero amount
                if t == 0:
                    dp[i][t] = 0
                # * if you use elifs, fails
                if i > 0:
                    # * Exclude the coin: In this case, we will take the minimum coin count from the previous set
                    dp[i][t] = dp[i - 1][t]

                if t >= coin:
                    # * include the coin
                    # * dp[i][t-coin] + 1: take the minimum count needed to get the remaining total, plus include ‘1’ for the current coin
                    # ! min(dp[i][t] because we already computed min value up there.
                    dp[i][t] = min(dp[i][t], dp[i][t - coin] + 1)
        # print(dp)
        # amount combinations will be at the bottom-right corner.
        return -1 if dp[n - 1][amount] == math.inf else dp[n - 1][amount]
