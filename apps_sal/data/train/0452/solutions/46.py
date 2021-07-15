class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        max_table = [[0]*n for _ in range(n)]
        for i in range(n):
            max_table[i][i] = jobDifficulty[i]
            for j in range(i+1,n):
                max_table[i][j] = max(max_table[i][j-1], jobDifficulty[j])
        
        memo = [[0]*n for _ in range(d)]
        
        for j in range(n):
            memo[0][j] = max_table[0][j]
        
        for i in range(1, d):
            #memo[i][i] = max_table[i][i]
            for j in range(i,n):
                memo[i][j] = min(memo[i-1][t] + max_table[t+1][j] for t in range(i-1,j))
        
        return memo[-1][-1]
        

