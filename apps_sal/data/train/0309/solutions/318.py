class Solution:

    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dif = A[j] - A[i]
                if (i, dif) in dp:
                    dp[j, dif] = dp[i, dif] + 1
                else:
                    dp[j, dif] = 2
        return max(dp.values())
