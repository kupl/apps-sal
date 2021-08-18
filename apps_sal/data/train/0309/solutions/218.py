class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
