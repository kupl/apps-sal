class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        if n == d:
            return sum(jobDifficulty)
        
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        for i in range(1, n + 1):
            dp[1][i] = max(jobDifficulty[:i])
            
        for _d in range(2, d + 1):
            for i in range(_d, n + 1):
                for j in range(_d - 1, i):
                    dp[_d][i] = min(dp[_d][i], dp[_d - 1][j] + max(jobDifficulty[j:i]))
                    
        return dp[d][n]
