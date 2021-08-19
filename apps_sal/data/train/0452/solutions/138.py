class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            (maxd, res) = (0, float('inf'))
            for j in range(i, len(jobDifficulty) - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)
