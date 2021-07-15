class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        dp = [0]+[float('inf')]*N
        
        for i in range(1, d+1):
            dp2 = [float('inf')]*(N+1)
            stack = []
            for j in range(i, N+1-d+i):
                curr_max = jobDifficulty[j-1]
                if i==1:
                    dp2[j] = max(jobDifficulty[:j])
                else:
                    dp2[j] = dp[j-1]+curr_max
                    
                while stack and stack[-1][1]<=curr_max:
                    dp2[j] = min(dp2[j], dp2[stack[-1][0]]-stack[-1][1]+curr_max)
                    stack.pop()
                    
                if stack and dp2[stack[-1][0]]<dp2[j]:
                    dp2[j] = dp2[stack[-1][0]]
                    curr_max = stack[-1][1]
                
                stack.append((j, curr_max))
            dp = dp2
        return dp[N] if dp[N]!=float('inf') else -1    

