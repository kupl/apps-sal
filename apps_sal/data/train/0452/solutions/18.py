class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        cumsum = [0] * len(jobDifficulty)
        cummax = [[0] * len(jobDifficulty) for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            cumsum[i] = cumsum[i - 1] + jobDifficulty[i]
            for j in range(i, len(jobDifficulty)):
                cummax[i][j] = max(cummax[i][j - 1], jobDifficulty[j])
        memo = {}

        @lru_cache()
        def DFS(s, d):
            if (s, d) in memo:
                return memo[s, d]
            if d > s:
                memo[s, d] = float('inf')
            elif d == s:
                memo[s, d] = cumsum[s - 1]
            elif d == 1:
                memo[s, d] = cummax[0][s - 1]
            else:
                memo[s, d] = min((cummax[i][s - 1] + DFS(i, d - 1) for i in range(1, s)))
            return memo[s, d]
        res = DFS(len(jobDifficulty), d)
        return res if res < float('inf') else -1
