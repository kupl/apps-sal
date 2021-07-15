class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins.sort()
        dp = [0] + [-1] * amount
        #print(dp)
        for coin in coins:
            for idx in range(coin, len(dp)):    
                if dp[idx - coin] != -1:
                    if dp[idx] != -1:
                        dp[idx] = min(dp[idx - coin] + 1, dp[idx])
                    else:
                        dp[idx] = dp[idx - coin] + 1
        #print(dp)
        return dp[amount]

