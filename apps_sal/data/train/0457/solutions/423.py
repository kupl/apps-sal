class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] means how many coins we need to make up i money
        # formula: dp[i] = min(dp[i - k] + 1 for k in coins)
        # start point: dp[i] = 1 if i in coins
        # we can add a 1 offset here since dp[0] doesn't make any sense
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
