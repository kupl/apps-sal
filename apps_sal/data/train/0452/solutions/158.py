class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)

        matrix = [[0] * len(jobDifficulty) for i in range(len(jobDifficulty))]

        for i in range(1, len(jobDifficulty) + 1):
            for j in range(len(jobDifficulty)):
                if i + j - 1 >= len(jobDifficulty):
                    continue
                matrix[j][i + j - 1] = max(jobDifficulty[i + j - 1], matrix[j][i + j - 2] if i > 1 else 0)

        dp = [[float('inf')] * (len(jobDifficulty) + 1) for i in range(d + 1)]

        for i in range(1, d + 1):
            for j in range(1, len(jobDifficulty) + 1):
                if i == 1:
                    dp[i][j] = matrix[0][j - 1]
                elif j > 1:
                    dp[i][j] = min([dp[i - 1][j - k] + matrix[j - k + 1 - 1][j - 1] for k in range(1, j)])

        return dp[-1][-1]
