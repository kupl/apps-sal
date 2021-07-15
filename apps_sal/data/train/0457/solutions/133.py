class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[sys.maxsize]*(amount+1)
        
        dp[0]=0
        for i in range(1,len(dp)):
            for c in coins:
                if c<=i:
                    dp[i]=min(dp[i],dp[i-c]+1)
                    
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]
            
        
        

