class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [-1 for _ in range(amount)]
        coins = set(coins)
        for i in range(amount):
            if (i + 1) in coins:
                dp[i] = 1
                continue
            for coin in coins:
                if (i - coin) >= 0 and dp[i - coin] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1]
