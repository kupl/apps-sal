class Solution:
    def numRollsToTarget(self, d, f, target):
        '''
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        '''
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(d + 1):
            for t in range(1, target + 1):
                for val in range(1, min(f, t) + 1):
                    dp[i][t] = (dp[i][t] + dp[i - 1][t - val]) % mod
        return dp[d][target]
