class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        s = len(A)
        dp = {}
        for i in range(s):
            for j in range(i+1, s):
                diff = A[j] - A[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
        return max(dp.values())
