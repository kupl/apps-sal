class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins_dict = {coin, coin for coin in coins}
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                low = float('inf')
                for coin in coins:
                    if i - coin >= 0 and dp[i - coin] != -1:
                        dp[i] = min(low, 1 + dp[i - coin])
                        low = min(low, 1 + dp[i - coin])
        print(dp)
        return dp[-1]
