class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        M = 10**9+7
        dp = [[0 for j in range(max(target, f)+1)] for i in range(d+1)]
        for j in range(1, f+1):
            dp[1][j] = 1
            
        for i in range(2, d+1):
            for j in range(i, max(target, f)+1):
                # print(\"i\", i, \"j\", j)
                for k in range(1, f+1):
                    if j>=k:
                        dp[i][j] += dp[i-1][j-k]
        
            
        # for i in range(d+1):
        #     print(dp[i])
            
        return dp[-1][target] % M
    
# 1
# 6
# 3
# 2
# 6
# 7
# 2
# 5
# 10
# 30
# 30
# 500

