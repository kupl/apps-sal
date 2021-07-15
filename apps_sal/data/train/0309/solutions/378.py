class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        n = len(A)
        res = 2
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                dp[d, i] = dp.get((d, j), 1) + 1
                res = max(res, dp[d, i])
        return res
                

