class Solution:    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dpt = [[1 if (i == 0 and 0<j and j <= f) else 0 for j in range(target+1)] for i in range(d)]
        for i in range(1,d):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if(j-k >= 0):
                        dpt[i][j] += dpt[i-1][j-k] % (10**9+7)
        return dpt[-1][target] % (10**9+7)
        

