class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        dp = [[float('inf')] * (d + 1) for _ in range(len(jobDifficulty))]
        tempmax = 0
        for i, job in enumerate(jobDifficulty):
            tempmax = max(tempmax, job)
            dp[i][1] = tempmax
        for day in range(2, d + 1):
            for j in range(day - 1, len(jobDifficulty)):
                result = float('inf')
                tempmax = 0
                for k in range(j, day - 3, -1):
                    tempmax = max(tempmax, jobDifficulty[k])
                    result = min(result, dp[k - 1][day - 1] + tempmax)
                dp[j][day] = result
        return dp[-1][-1]
