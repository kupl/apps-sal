class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        (dp, n, ans) = ({}, len(A), 0)
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
                ans = max(ans, dp[j, diff])
        return ans
