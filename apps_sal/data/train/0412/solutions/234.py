class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dice = [k for k in range(1,f+1)]
        dp = [[0 for _ in range(d+1)]for _ in range(target+1)]
        
        def numRolls(d,f,target):
            for j in range(1,min(f+1,target+1)): dp[j][1] = 1
            for i in range(2,d+1):
                for j in range(1,target+1):
                    for new_t in list(map(lambda k: j-k,dice)):
                        if new_t >= 0 :
                            dp[j][i] += dp[new_t][i-1]
                        dp[j][i] 
            return dp[target][d]% (10**9 + 7)
        
                        
        return numRolls(d,f,target)
