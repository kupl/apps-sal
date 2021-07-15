class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        if not jobDifficulty or len(jobDifficulty)<d: return -1
        
        @lru_cache(None)
        def dp(start, rem):
            
            if rem==0:
                return 0 if start >= len(jobDifficulty) else math.inf
            if start >= len(jobDifficulty):
                return 0 if rem == 0 else math.inf
            
            maxDiff = -math.inf
            minDiff = math.inf
            
            for i in range(start, len(jobDifficulty)):
                maxDiff = max(maxDiff, jobDifficulty[i])
                minDiff = min(minDiff, maxDiff+dp(i+1, rem-1))
            
            return minDiff
        
        ans = dp(0, d)
        return ans if ans != math.inf else -1
        
        # [6,5,4,3,2,1] d=2

