class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        if not A:
            return 0

        n = len(A)
        dp = dict()

        for r in range(1, n):
            for l in range(r):
                dp[r, A[r] - A[l]] = dp.get((l, A[r] - A[l]), 1) + 1

        return max(dp.values())
