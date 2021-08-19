class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        d = {}
        res = 0
        for i in range(n):
            d[i] = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in d[j]:
                    d[i][diff] = 2
                else:
                    d[i][diff] = d[j][diff] + 1
                res = max(res, d[i][diff])
        return res
