class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ret = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1
                ret = max(ret, dp[i, diff])
        return ret
