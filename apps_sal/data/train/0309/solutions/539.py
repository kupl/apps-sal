class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        (dp, res) = ({}, 0)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
                res = max(res, dp[j, A[j] - A[i]])
        return res
