class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = []
        for a in range(d + 1):
            dp.append([-1] * (n + 1))

        def helper(jobD, n, d, dp):
            if n < d:
                return -1
            if dp[d][n] != -1:
                return dp[d][n]
            if d == n:
                dp[d][n] = sum(jobD[0:n])
                return dp[d][n]
            if d == 1:
                dp[d][n] = max(jobD[0:n])
                return dp[d][n]
            for i in range(1, n):
                r = helper(jobD, i, d - 1, dp)
                if r != -1:
                    if dp[d][n] == -1:
                        dp[d][n] = r + max(jobD[i:n])
                    else:
                        dp[d][n] = min(dp[d][n], r + max(jobD[i:n]))
            return dp[d][n]

        r = helper(jobDifficulty, n, d, dp)
        return r
