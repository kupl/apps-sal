class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        dp = [[0 for i in range(d)] for j in range(len(jobDifficulty))]
        for j in range(len(jobDifficulty)):
            dp[j][0] = max(jobDifficulty[:j + 1])
        for day in range(1, d):
            for i in range(day, len(jobDifficulty)):
                dpValue = sum(jobDifficulty)
                for j in range(day - 1, i):
                    dpValue = min(dpValue, dp[j][day - 1] + max(jobDifficulty[j + 1:i + 1]))
                dp[i][day] = dpValue
        return dp[len(jobDifficulty) - 1][d - 1]
