class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 0-1 bag, dp[i][j] is the minimum number of coins only use the first i coins can sum up to target j
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if i == coin:
                    dp[i] = 1
                elif dp[i] == -1 and dp[i - coin] != -1:
                    dp[i] = dp[i - coin] + 1
                elif dp[i] != -1 and dp[i - coin] != -1:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1]
