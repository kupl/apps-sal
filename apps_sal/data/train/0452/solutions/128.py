class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        from functools import lru_cache
        @lru_cache(None)
        def helper(jobs, d):
            if d==1:
                return max(jobs)
            mn=float('inf')
            for i in range(1, len(jobs)-d+2):
                s = max(jobs[:i])+helper(jobs[i:],d-1)
                mn = min(s, mn)
            return mn
        res = helper(tuple(jobDifficulty), d)
        return res if res!=float('inf') else -1
                

