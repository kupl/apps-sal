class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)
        
        if n < d:
            return -1
        
        dp = [[-1 for i in range(d+1)] for j in range(n)]
        
        def helper(i, days):

            nonlocal dp

            if dp[i][days] != -1:
                return dp[i][days]
            
            
            if days == 1:
                dp[i][days] = max(jobDifficulty[i:])
            else:
                dp[i][days] = min([max(jobDifficulty[i:i+j]) + helper(i+j, days-1) for j in range(1, n-days-i+2)])
                
            return dp[i][days]
        
        return helper(0, d)

