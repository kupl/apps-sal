class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        (n, dp) = (len(A), {})
        for i in range(n):
            for j in range(i + 1, n):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
