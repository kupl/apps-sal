class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(0, amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[-1] <= amount:
            return dp[-1]
        else:
            return -1
