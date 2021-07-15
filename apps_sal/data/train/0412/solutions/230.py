class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        dp=[[0]*(target+1) for _ in range(d+1)]
        md=pow(10,9)+7
        dp[0][0]=1
        for trial in range(1,d+1):
            for i in range(target):
                for face in range(1,f+1):
                    if i+face<=target:
                        dp[trial][i+face]+=dp[trial-1][i]
                        dp[trial][i+face]%=md
        
        return dp[-1][target]
            

