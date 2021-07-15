class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins = sorted(coins)
                
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        
        for coin in coins:
            for a in range(coin, amount+1):
                dp[a] = min(dp[a], dp[a-coin]+1)
                            
        res = dp[amount] if dp[amount] < amount+1 else -1
            
        return res

