class Solution:

    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [{} for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if d in dp[i]:
                    dp[j][d] = dp[i][d] + 1
                else:
                    dp[j][d] = 2
                res = max(res, dp[j][d])
        return res
