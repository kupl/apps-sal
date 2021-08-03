class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}

        for i, a in enumerate(A[1:], 1):
            for j, b in enumerate(A[:i]):
                d = a - b
                dp[i, d] = dp.get((j, d), 0) + 1

        return max(dp.values()) + 1
