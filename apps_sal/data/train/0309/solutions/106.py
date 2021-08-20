class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                delta = A[j] - A[i]
                if (delta, i) in dp:
                    dp[delta, j] = dp[delta, i] + 1
                else:
                    dp[delta, j] = 2
        return max(dp.values())
