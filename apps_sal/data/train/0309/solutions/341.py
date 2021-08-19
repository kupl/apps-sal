class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ret = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[i] - A[j]
                dp[j, diff] = dp.get((i, diff), 1) + 1
                ret = max(ret, dp[j, diff])
        return ret
