class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x = dp.get((i, A[j] - A[i]), 1)
                dp[j, A[j] - A[i]] = x + 1
        return max(dp.values())
