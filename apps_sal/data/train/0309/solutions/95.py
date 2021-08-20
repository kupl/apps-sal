class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                delta = A[j] - A[i]
                dp[j, delta] = dp[i, delta] + 1 if (i, delta) in dp else 2
        return max(dp.values())
