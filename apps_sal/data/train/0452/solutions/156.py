class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}
        n = len(jobDifficulty)
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    memo[i, j] = jobDifficulty[i]
                else:
                    memo[i, j] = max(memo[i, j - 1], jobDifficulty[j])
        if n < d:
            return -1

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return memo[i, n - 1]
            res = float('inf')
            for j in range(i, n - d + 1):
                res = min(res, memo[i, j] + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)
