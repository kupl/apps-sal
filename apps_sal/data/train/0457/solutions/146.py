class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)
        res = dp[amount] if dp[amount] < amount + 1 else -1
        return res
