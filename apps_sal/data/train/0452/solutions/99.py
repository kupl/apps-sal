class Solution:
    def minDifficulty(self, jobDifficulty, d):
        '''
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        '''
        njobs = len(jobDifficulty)
        if njobs < d:
            return -1

        dp = [[float('inf')] * njobs for _ in range(d)]
        # base case
        for j in range(njobs):
            dp[0][j] = max(jobDifficulty[:j + 1])

        for i in range(1, d):
            for j in range(i, njobs):
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + max(jobDifficulty[k:j + 1]))
        return dp[d - 1][njobs - 1]
