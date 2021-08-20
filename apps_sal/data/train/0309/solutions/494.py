class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for a in A]
        imax = 1
        for i in range(len(A)):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                prev = dp[i].get(diff, 1)
                dp[i][diff] = max(dp[j].get(diff, 1) + 1, prev)
                imax = max(imax, dp[i][diff])
        return imax
