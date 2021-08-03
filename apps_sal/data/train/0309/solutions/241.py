class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        n = len(A)
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2

        return max(dp.values())
