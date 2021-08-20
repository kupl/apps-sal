class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) == 2:
            return len(A)
        d = [{} for i in range(len(A))]
        m = 0
        for i in range(1, len(A)):
            for j in range(i):
                k = A[i] - A[j]
                if k in d[j]:
                    d[i][k] = max(2, 1 + d[j][k])
                else:
                    d[i][k] = 2
                m = max(m, d[i][k])
        return m
