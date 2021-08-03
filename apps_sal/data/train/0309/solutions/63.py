class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        N = len(A)
        for i, n in enumerate(A):
            for j in range(i + 1, N):
                b = A[j] - n
                if (i, b) in dp:
                    dp[j, b] = dp[i, b] + 1
                else:
                    dp[j, b] = 2

        return max(dp.values())
