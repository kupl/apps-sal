class Solution:
    def longestArithSeqLength(self, A):
        dp = collections.defaultdict(int)
        mx = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                j_key = (j, diff)
                i_key = (i, diff)
                
                dp[i_key] = max(2, dp[j_key]+1)
        return max(dp.values())
