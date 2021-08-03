class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)

        matrix = [[0] * len(jobDifficulty) for i in range(len(jobDifficulty))]

        for i in range(len(jobDifficulty)):
            for j in range(i, len(jobDifficulty)):
                if i == j:
                    matrix[i][j] = jobDifficulty[j]
                else:
                    matrix[i][j] = max(matrix[i][j - 1], jobDifficulty[j])

        dp = [[float('inf')] * len(jobDifficulty) for i in range(d)]

        for i in range(d):
            for j in range(i, len(jobDifficulty)):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if j > 0:
                        dp[i][j] = min([matrix[j - k][j] + dp[i - 1][j - k - 1] for k in range(0, j)])

        return dp[-1][-1]
