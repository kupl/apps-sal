class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        if amount in coins:
            return 1
        dp = [float('inf')] * (amount + 1)
        for coin in coins:
            if coin < amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if coin < i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
