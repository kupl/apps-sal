class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [1]+[0]*target
        
        for i in range(1, d+1):
            dp2 = [0]*(target+1)
            for j in range(target, i-1, -1):
                for k in range(1, f+1):
                    if j-k<i-1: break
                    
                    dp2[j] += dp[j-k]
                dp2[j]%=(10**9+7)
            dp = dp2
        # print(dp)
        return dp[-1]
