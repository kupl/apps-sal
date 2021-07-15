class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d: 
            return -1
        
        dp = [jobDifficulty[0]]
        for j in jobDifficulty[1:]:
            dp.append(max(dp[-1], j))

        for i in range(1, d):
            
            dp_curr = [0] * N
            
            stack = []
            for j in range(i, N):
                dp_curr[j] = dp[j - 1] + jobDifficulty[j]
                
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[j]:
                    dp_curr[j] = min(dp_curr[j], dp_curr[stack[-1]] - jobDifficulty[stack[-1]] + jobDifficulty[j])
                    stack.pop()
                    
                if stack:
                    dp_curr[j] = min(dp_curr[j], dp_curr[stack[-1]]) 
                stack.append(j)
                
            dp = dp_curr
        return dp[-1]
