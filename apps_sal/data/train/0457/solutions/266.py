class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins and amount==0: return 1
        if not coins: return 0
        
        dp = [float('inf')]*(amount+1) 
        dp[0]=0
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j-coins[i-1]>=0:
                        dp[j] = min(dp[j], dp[j-coins[i-1]]+1)         
        return dp[-1] if dp[-1]!=float('inf') else -1


