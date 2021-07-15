class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = {}
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2
        return max(dp.values())
