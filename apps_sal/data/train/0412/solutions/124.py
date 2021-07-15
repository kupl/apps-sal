class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        
        dp[0][0] = 1
        
        # Iterate through every dice
        for i in range(1, d+1):
            
            # iterate through every target
            for j in range(1, target+1):
                
                # go through every possible value on dice
                for k in range(1, f+1):
                    if k <= j:
                        dp[i][j] += dp[i-1][j - k]
                        
        return dp[-1][-1] % (10**9 + 7)
