class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        A = jobDifficulty
        n = len(A)

        if d > n:  # more days than job
            return -1

        dp = [[math.inf] * (d + 1) for _ in range(n)]
        # dp[i][j] store the ans for jobs i:n with j days remaining

        for i in range(n - 1, -1, -1):
            for j in range(1, d + 1):
                if n - i < j:  # more days than jobs
                    continue
                rMax = -math.inf
                for k in range(i, n - j + 1):  # if we finish i:k+1 jobs today
                    rMax = max(rMax, A[k])
                    if j == 1:
                        dp[i][j] = rMax
                    else:
                        dp[i][j] = min(dp[i][j], rMax + dp[k + 1][j - 1])
        return dp[0][d]
