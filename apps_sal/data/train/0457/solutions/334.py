class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount):
            mn = math.inf
            pos = False
            for c in coins:
                if i+1>=c and dp[i-c+1]>=0:
            
                    pos = True
                    mn = min(mn, dp[i+1-c]+1)
           
            if pos:
                dp[i+1] = mn
          
      
        return dp[-1]
                    
                    

