class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M = 10**9+7
        memo = [[0]*sum(rollMax) for _ in range(n)]
        start = {0:0}
        for i in range(1, len(rollMax)):
            start[i] = start[i-1] + rollMax[i-1]
            
        
        
        for i in range(len(rollMax)):
            s = start[i]
            memo[0][s] = 1
        
        for i in range(1, n):
            for j in range(len(rollMax)):
                s = start[j]
                e = start[j] + rollMax[j]-1
                memo[i][s] = (sum(memo[i-1][:s])+sum(memo[i-1][e+1:])) % M
                for k in range(1,rollMax[j]):
                    memo[i][s+k] = memo[i-1][s+k-1]
        
        return sum(memo[-1]) % M

