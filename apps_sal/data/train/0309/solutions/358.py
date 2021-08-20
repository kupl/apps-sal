class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        res = 0
        for i in range(len(A)):
            for j in range(i):
                x = A[i] - A[j]
                dp[i][x] = max(dp[j][x] + 1 if x in dp[j] else 0, 2 if x not in dp[i] else dp[i][x])
                res = max(dp[i][x], res)
        return res
