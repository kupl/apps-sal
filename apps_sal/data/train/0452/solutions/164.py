class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        @lru_cache(None)
        def dfs(index, d):
            if index == len(jobDifficulty) and d == 0:
                return 0
            
            if d == 0 and index < len(jobDifficulty):
                return float('inf')
            
            temp = float('inf')
            curr = 0
            for i in range(index, len(jobDifficulty)):
                curr = max(curr, jobDifficulty[i])
                temp = min(temp, curr + dfs(i + 1, d - 1))
            
            return temp
        
        return dfs(0, d)
