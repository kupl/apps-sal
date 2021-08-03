class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        res = 0
        dp = [{} for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])

        return res
