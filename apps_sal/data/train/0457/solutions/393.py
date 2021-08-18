class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        coins = sorted(coins)

        dp = {coin: 1 for coin in coins}

        def helper(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            dp[amount] = float('inf')
            for i in range(len(coins) - 1, -1, -1):
                if amount - coins[i] >= 0:
                    dp[amount] = min(dp[amount], 1 + helper(amount - coins[i]))

            return dp[amount]

        result = helper(amount)
        if result == float('inf'):
            return -1
        else:
            return result
