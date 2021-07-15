class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # @lru_cache(None)
        # def helper(start, d):
        #     if len(jobDifficulty) - start < d:
        #         return float('inf')
        #     if d == 1:
        #         return max(jobDifficulty[start:])
        #     result = float('inf')
        #     for i in range(start, len(jobDifficulty) - d + 1):
        #         result = min(result, max(jobDifficulty[start:i+1]) + helper(i+1, d-1))
        #     return result
        # result = helper(0, d)
        # return result if result != float('inf') else -1
        if len(jobDifficulty) < d:
            return -1
        dp = [[float('inf')] * (d + 1) for _ in range(len(jobDifficulty))]
        tempmax = 0
        for i, job in enumerate(jobDifficulty):
            tempmax = max(tempmax, job)
            dp[i][1] = tempmax
        for day in range(2, d+1):
            for j in range(day-1, len(jobDifficulty)+1):
                result = float('inf')
                for k in range(j-1):
                    result = min(result, dp[k][day-1] + max(jobDifficulty[k+1:j]))
                dp[j-1][day] = result
        return dp[-1][-1]

