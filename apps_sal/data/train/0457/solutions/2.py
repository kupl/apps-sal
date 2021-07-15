class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INVALID = 2**32
        dp = [INVALID] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] >= dp[i]: continue
                dp[i] = dp[i - coin] + 1
        return -1 if dp[amount] == INVALID else dp[amount]
