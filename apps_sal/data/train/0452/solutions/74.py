class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)
        memo = {}
        
        if d > n:
            return -1
        if d == n:
            return sum(jobDifficulty)
        
        def dfs(i, diff, days):
            if i == n:
                return diff if days == 0 else float('inf')
            
            if (i, diff, days) in memo:
                return memo[(i, diff, days)]
            
            max_effort = max(diff, jobDifficulty[i])
            
            s1 = max_effort + dfs(i+1, 0, days-1)
            s2 = dfs(i+1, max_effort, days)
            
            memo[(i, diff, days)] = min(s1, s2)
            
            return memo[(i, diff, days)]
        
        return dfs(0, 0, d)
