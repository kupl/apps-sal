class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount==0:
            return 0
        
        
        if len(coins)==1:
            
            if amount%coins[0]==0:
                return amount//coins[0]
            return -1
        
        dp=[0]*(amount+1)
        
        for i in range(1,amount+1):
            
            if i in set(coins):
                dp[i]=1
                continue
                
            min_coins=float('inf')
            
            for coin in coins:
                
                if i-coin>=0:
                    min_coins=min(dp[i-coin],min_coins)
                    
            dp[i]=min_coins+1
            
            
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
                    
    
    
                                 
                   
                

