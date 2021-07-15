class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        if d*f < target:
            return 0
        elif d*f == target:
            return 1
        
        dp = [[0]*(target+1) for _ in range(d+1)]
        for i in range(1, min(f+1, target+1)):
            dp[1][i] = 1
        
        print(dp)
        
        for i in range(1,d+1):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if k <= j:
                        dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= (10**9+7) 
            
        print(dp)
        return dp[-1][-1] 
