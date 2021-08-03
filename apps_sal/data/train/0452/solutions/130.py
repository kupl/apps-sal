class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if d > N:
            return -1
        memo = [[float('inf')] * (d + 1) for _ in range(N + 1)]
        memo[0][0] = 0
        for i in range(1, N + 1):
            for k in range(1, min(i, d) + 1):
                memo[i][k] = min(memo[j][k - 1] + max(jobDifficulty[j:i]) for j in range(i - 1, -1, -1))
        return memo[N][d]
