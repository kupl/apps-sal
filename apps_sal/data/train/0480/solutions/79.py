class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0 for _ in range(arrLen)]
        dp[0],dp[1]=1,1
        for s in range(2,steps+1):
            dp2 = [0 for _ in range(min(steps-s+2,arrLen))]
            dp2[0]= dp[0]+dp[1]
            if arrLen !=1:
                dp2[-1]= dp[-2]+dp[-1]
            for num in range(1,min(steps-s+1,arrLen-1)):
                dp2[num] = dp[num-1]+dp[num]+dp[num+1]
            dp = dp2
            
        return(dp[0])%(10**9+7)
    

