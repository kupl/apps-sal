class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        from functools import lru_cache
        @lru_cache(None)
        def helper(st, d):
            if d==1:
                return max(jobDifficulty[st:])
            mn=float('inf')
            for i in range(st+1, len(jobDifficulty)-d+2):
                s = max(jobDifficulty[st:i])+helper(i,d-1)
                mn = min(s, mn)
            return mn
        res = helper(0, d)
        return res if res!=float('inf') else -1
                

