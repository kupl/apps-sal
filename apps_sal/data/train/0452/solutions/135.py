class Solution:
    def minDifficulty(self, job_dif, d: int) -> int:
        len_job = len(job_dif)
        if d > len_job: return -1
        len_job += 1
        dp = [[float('inf')] * (d + 1) for _ in range(len_job)]
        job_dif = [0] + job_dif
        dp[0][0] = 0
        
        for i in range(1, len_job):
            for k in range(1, min(i+1, d+1)):
                for j in range(k, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + max(job_dif[j:i+1]))
        return dp[-1][-1]
