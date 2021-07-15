class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        #dp[0][0] = 1
        
        for i in range(1, d+1):
            new = [0]
            for j in range(1, target+1):
                new.append(0)
                for k in range(1, f+1):
                    if j-k>=0:
                        new[-1]=(new[-1]+dp[j-k])%(10**9+7)
                        #dp[i][j]+=dp[i-1][j-k]
                    else:
                        break
            dp = new             
        return dp[-1]
        return dp[-1][-1]%(10**9+7)
                
                
    
    '''
    f = 6
    
     01234567
    010000000
    101111110
    200123456
         
         
         
    '''
