class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Sol.3 - DP (Bottom up)
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i and (dp[i] > dp[i-coin]+1):
                    dp[i] = dp[i-coin] + 1

        return dp[amount] if dp[amount] != (amount + 1) else -1
    
    

