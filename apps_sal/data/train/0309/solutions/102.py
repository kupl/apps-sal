class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                d = A[j] - A[i]
                dp[j, d] = dp.get((i, d), 1) + 1
        return max(dp.values())
