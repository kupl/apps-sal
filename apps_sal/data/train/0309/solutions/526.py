class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        imax = 1
        for i in range(len(A)):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                prev = dp.get((diff, i), 1)
                saved = dp[diff, i] = max(dp.get((diff, j), 1) + 1, prev)
                imax = max(imax, saved)
        return imax
