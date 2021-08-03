class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        length = len(A)

        for i in range(length):
            for j in range(i + 1, length):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1

        return max(dp.values())
