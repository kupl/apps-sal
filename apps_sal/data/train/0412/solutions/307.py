class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0]*(target+1)
        
        for i in range(1,f+1):
            if i<=target:
                dp[i] = 1
        temp = dp[:]
        for i in range(1,d):
            dp = [0]*(target+1)

            for t in range(1, target+1):              
                if temp[t]>0:
                    for k in range(1,f+1):
                        if t+k <= target:
                            dp[t+k]+= temp[t]%(10**9 + 7) 
           
            for t in range(1,target+1):
                dp[t]=dp[t]  %(10**9 + 7) 
            temp = dp[:]
    #    print(929256393%(10**9 + 7) )
        return dp[target]%(10**9 + 7) 

