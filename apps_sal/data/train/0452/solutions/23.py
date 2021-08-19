class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        cumsum = [0] * len(jobDifficulty)
        cummax = [[0] * len(jobDifficulty) for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            cumsum[i] = cumsum[i - 1] + jobDifficulty[i]
            for j in range(i, len(jobDifficulty)):
                cummax[i][j] = max(cummax[i][j - 1], jobDifficulty[j])

        @lru_cache(maxsize=None)
        def DFS(s, d):
            if d > s:
                return float('inf')
            elif d == s:
                return cumsum[s - 1]
            elif d == 1:
                return cummax[0][s - 1]
            else:
                return min((cummax[i][s - 1] + DFS(i, d - 1) for i in range(1, s)))
        res = DFS(len(jobDifficulty), d)
        return res if res < float('inf') else -1
