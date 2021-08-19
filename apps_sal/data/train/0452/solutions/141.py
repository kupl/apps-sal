class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        elif d == n:
            return sum(jobDifficulty)
        else:
            "\n                1. can only do job i if job[0] ~ job[i-1] are done\n                2. if cur job is t(i), we can put t(i+1) ~ t(j - 1) into the same day while t(i + 1) ~ t(j - 1) are all smaller than t(i)\n                3. if t(j) >= t(i), then we must make a choice\n                4. should we start from the end of the jobs? \n                    -> should be the same\n                5. this should be a knapsack problem. \n                    -> for each day and each task, should we do it in the cur day? or the next day?                \n                    -> and there will be the same node -> need memo\n                    -> can we do bottom up?\n\n                6. \n                    dateIndex = 0 ~ (d - 1)\n                    jobStartIndex = 0 ~ (n - 1)           \n\n                    dp[i][j]: the min cost at day i, job j                    \n                    dp[i][j] = min(today's cost + future cost)\n                                = min( \n                                        only do job-j: \n                                            jobDifficulty[j] + dp[i + 1][j + 1]\n                                        do job-j, job-j + 1:\n                                            max(jobDifficulty[j], jobDifficulty[j + 1]) + dp[i + 1][j + 2]                                        \n                                        ...\n\n                                        do max(jobDifficulty[j],..., jobDifficulty[n - 1]) + dp[i + 1][n]                                        \n                                        )\n                    so we need to do i + 1 first and j + 1 first            \n            "
            n = len(jobDifficulty)
            dp = dict()
            for d in range(0, d + 1):
                dp[d] = dict()
                for j in range(0, n + 1):
                    dp[d][j] = float('inf')
            dp[d][n] = 0
            for i in range(d - 1, -1, -1):
                for j in range(n - 1, i - 1, -1):
                    for k in range(j, n):
                        futureCost = dp[i + 1][k + 1]
                        todayCost = max(jobDifficulty[j:k + 1])
                        dp[i][j] = min(dp[i][j], todayCost + futureCost)
            return dp[0][0]
