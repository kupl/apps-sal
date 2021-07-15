class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        def dfs(i, d, visit):
            if i == len(jobDifficulty):
                return float('inf')
            if d == 1:
                return max(jobDifficulty[i:])
            if (i, d) in visit:
                return visit[(i,d)]
            
            res = float('inf')
            cur = 0
            for j in range(i, len(jobDifficulty)):
                cur = max(cur, jobDifficulty[j])
                res = min(res, cur + dfs(j+1, d-1, visit))
            visit[(i,d)] = res
            return res
        return dfs(0,d,{})
