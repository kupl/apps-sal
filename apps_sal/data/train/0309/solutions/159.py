class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [{} for _ in range(n)]
        res = 0
        for j in range(n):
            for i in range(j):
                d = A[j] - A[i]
                if d in dp[i]:
                    dp[j][d] = dp[i][d] + 1
                else:
                    dp[j][d] = 2
                res = max(res, dp[j][d])
        return res
