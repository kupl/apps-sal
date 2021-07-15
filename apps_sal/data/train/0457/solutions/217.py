class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[None]*(amount+1)
        dp[0]=0
        n= len(coins)
        for coin in coins:
            if coin<= amount:
                dp[coin]=1
        for i in range(1,amount+1):
            if i in coins:
                continue
            tmp= float('inf')
            for coin in coins:
                
                if coin<= i:
                    if dp[i-coin]==-1:
                        continue
                    else:                        
                        tmp= min(tmp,1+dp[i-coin])
                else:
                    continue
            if tmp==float('inf'):
                dp[i]=-1
            else:
                dp[i]=tmp
        print(dp)        
        return dp[-1]
        

