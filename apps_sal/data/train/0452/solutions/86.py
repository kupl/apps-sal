class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        @lru_cache(None)
        def dp(start, k):
            
            if k == 1:
                return max(jobDifficulty[start:])
            
            minvalue = float('inf')
            for i in range(start+1, n):
                left = max(jobDifficulty[start:i])
                right = dp(i, k-1)
                
                minvalue = min(minvalue, left+right)
            
            return minvalue
        
        return dp(0,d)

