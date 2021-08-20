class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                if (i, diff) in dp:
                    dp[j, diff] = dp[i, diff] + 1
                else:
                    dp[j, diff] = 2
        return max(dp.values())
