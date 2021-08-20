class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in dp[i]:
                    dp[i][diff] = 2
                if diff in dp[j]:
                    dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                res = max(res, dp[i][diff])
        return res
