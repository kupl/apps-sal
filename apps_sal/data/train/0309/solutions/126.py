class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}

        for i in range(len(A)):
            for j in range(i):
                d = A[j] - A[i]
                dp[i, d] = dp.get((j, d), 0) + 1

        return max(dp.values()) + 1
