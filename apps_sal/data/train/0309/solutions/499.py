class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for i in range(len(A))]
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] = max(dp[i].get(A[i] - A[j], 0), dp[j].get(A[i] - A[j], 0) + 1)
                res = max(res, dp[i][A[i] - A[j]])
        return res + 1
