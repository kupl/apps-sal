class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for i in range(len(A))]
        res = 0
        for i in range(len(A)):
            for j in range(i):
                # in the case that we are attaching to a single element
                if A[i] - A[j] in dp[j]:
                    dp[i][A[i] - A[j]] = max(2, 1 + dp[j][A[i] - A[j]])
                else:
                    dp[i][A[i] - A[j]] = 2
                res = max(res, dp[i][A[i] - A[j]])
        return res
