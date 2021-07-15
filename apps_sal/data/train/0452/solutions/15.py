class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jc = len(jobDifficulty)
        if d > jc: return -1
        dp = [[-1 for i in range(jc+1)] for i in range(d+1)]
        dp[1][1] = jobDifficulty[0]

        for i in range(2, jc+1):
            dp[1][i] = max(dp[1][i-1], jobDifficulty[i-1])
        
        for i in range(2, d+1):
            for j in range(i, jc+1):
                dp[i][j] = dp[i-1][j-1] + jobDifficulty[j-1]
                work = jobDifficulty[j-1]
                for k in range(j-2, i-2, -1):
                    work = max(jobDifficulty[k], work)
                    if dp[i-1][k] + work < dp[i][j]:
                        dp[i][j] = dp[i-1][k] + work
        return dp[d][jc]



