class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*d for i in range(target + 1)]
        
        for i in range(1, target + 1):
            dp[i][0] = int(i <= f)
                
                   
        
        for dd in range(1, d):
            for ff in range(1, f+1):
                for i in range(target + 1):
                    if(i+ff <= target):
                        dp[i+ff][dd] = ( dp[i+ff][dd] + dp[i][dd-1] ) % mod
                        
            
        return dp[-1][-1]
