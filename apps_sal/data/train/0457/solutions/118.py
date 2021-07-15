class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for idx in range(coin, amount+1):
                # Get the coin count without this coin
                prev_coins_ct = dp[idx - coin]
                # Get the minimum of either adding from prev coin ct or current lowest
                dp[idx] = min(prev_coins_ct + 1, dp[idx])
        
        if dp[-1] == math.inf:
            return -1
        
        return dp[-1]
