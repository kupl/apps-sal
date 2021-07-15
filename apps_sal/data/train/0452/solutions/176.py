from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        @lru_cache(None)
        def dfs(idx, day):
            if day == 0:
                if idx < n:
                    return float('inf')
                else:
                    return 0
            tmp = 0
            res = float('inf')
            for j in range(idx, n):
                tmp = max(tmp, jobDifficulty[j])
                res = min(res, tmp + dfs(j + 1, day - 1))
            return res
        
        out = dfs(0, d)
        if out == float('inf'):
            return -1
        return out

