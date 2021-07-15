class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dpMatrix = [[0 for i in range(target+1)] for i in range(d)]
        
        for i in range(1,min(f+1, len(dpMatrix[0]))):
            dpMatrix[0][i] = 1
        
        for i in range(1,len(dpMatrix)):
            for j in range(1, len(dpMatrix[0])):
                calcSum=0
                for k in range(j-1, max(-1,j-f-1), -1):
                    calcSum+= dpMatrix[i-1][k]
                
                dpMatrix[i][j] = calcSum
        
        return dpMatrix[-1][-1]%(10**9 + 7)
