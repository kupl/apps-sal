class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return n
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
