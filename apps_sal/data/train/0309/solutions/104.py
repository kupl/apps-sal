class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = dict()
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                delta = A[j] - A[i]
                dp[j, delta] = dp.get((i, delta), 1) + 1
        return max(dp.values())
