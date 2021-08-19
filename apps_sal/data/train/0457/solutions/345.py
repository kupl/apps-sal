class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(i) = least coins that can sum up to i
        # iterate each coin on i to check if there's less number sums to i
        dp = [float('Inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float('Inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('Inf'):  # when the sum cannot be achieved
            return -1
        return dp[amount]
