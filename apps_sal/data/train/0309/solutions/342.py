class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        maxd = max(A) - min(A)
        dp = [[1 for j in range(2 * maxd + 1)] for i in range(len(A))]
        maxv = 1
        for i in range(1, len(dp)):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                maxv = max(maxv, dp[i][diff])
        return maxv
