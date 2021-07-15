class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, v in enumerate(A):
            for j in range(i):
                diff = v - A[j]
                dp.setdefault((diff, i), 1)
                dp[diff, i] = max(dp[diff, i], dp.get((diff, j), 1) + 1)
        return max(dp.values(), default=0)
