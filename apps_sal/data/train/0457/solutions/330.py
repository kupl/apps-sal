class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        '''
        [0,1,2,3,4,5,6,7,8,9,10]
        [0,1,1,2,2,1,2,2,3,3,2]
        
        '''
        
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for coin in coins:
            for num in range(coin, len(dp)):
                
                dp[num] = min(dp[num-coin] + 1, dp[num])
                
        return dp[amount] if dp[amount] != float('inf') else -1
