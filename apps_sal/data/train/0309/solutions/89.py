class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                gap = A[j] - A[i]
                if (i, gap) in dp:
                    dp[(j, gap)] = dp[(i, gap)] + 1
                else:
                    dp[(j, gap)] = 2

        return max(dp.values())
