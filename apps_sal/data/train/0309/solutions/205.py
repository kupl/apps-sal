class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [dict() for _ in range(len(A))]
        res = 2
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(dp[i][diff], res)
        return res
