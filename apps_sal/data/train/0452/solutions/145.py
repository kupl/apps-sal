class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        dp = [[float('inf') for _ in range(d + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):  # number of jobs, convert to index is i-1
            for k in range(1, d + 1):   # number of days
                for j in range(i - 1, k - 2, -1):  # j is job index: i-1 -> k-1
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + max(jobDifficulty[j:i]))
                    # 前j个job, k-1天 + i-j个job的max
        return dp[-1][-1]
