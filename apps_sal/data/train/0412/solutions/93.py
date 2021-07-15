class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        M = 10 ** 9  + 7
        for i in range(d):
            n_dp = [0] * (target + 1)
            for j in range(target + 1):
                for m in range(1, f + 1):
                    if j + m > target:
                        break
                    
                    n_dp[j + m] += dp[j]
            
            dp = [k % M for k in n_dp]
        
        return dp[-1]
