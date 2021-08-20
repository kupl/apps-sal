class Solution:

    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if (i, A[j] - A[i]) in dp:
                    dp[j, A[j] - A[i]] = dp[i, A[j] - A[i]] + 1
                else:
                    dp[j, A[j] - A[i]] = 2
        return max(dp.values())
