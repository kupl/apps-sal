class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @lru_cache(maxsize=None)
        def job_max(i, j):
            return max(jobDifficulty[i:j])

        @lru_cache(maxsize=None)
        def job_sum(i, j):
            return sum(jobDifficulty[i:j])

        @lru_cache(maxsize=None)
        def DFS(s, d):
            if d > s:
                return float('inf')
            if d == s:
                return job_sum(0, s)
            if d == 1:
                return job_max(0, s)

            return min(job_max(i, s) + DFS(i, d - 1) for i in range(1, s))

        res = DFS(len(jobDifficulty), d)
        return res if res < float('inf') else -1
