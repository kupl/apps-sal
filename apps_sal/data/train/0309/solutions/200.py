class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}

        for i in range(1, len(A)):
            for j in range(0, len(A[:i])):

                d = A[i] - A[j]

                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2

        return max(dp.values())
