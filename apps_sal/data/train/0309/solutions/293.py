class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        m = 2
        for i in range(1, len(A)):
            for j in range(0, i):
                if (j, A[i] - A[j]) in dp:
                    dp[(i, A[i] - A[j])] = dp[(j, A[i] - A[j])] + 1
                    m = max(m, dp[(i, A[i] - A[j])])
                else:
                    dp[(i, A[i] - A[j])] = 2
        return m
