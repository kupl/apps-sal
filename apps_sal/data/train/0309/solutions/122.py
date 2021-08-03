class Solution:
    def longestArithSeqLength(self, A):
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                j_key = (j, diff)
                i_key = (i, diff)
                if j_key in dp:
                    dp[i_key] = dp[j_key] + 1
                else:
                    dp[i_key] = 2
        return max(dp.values())
