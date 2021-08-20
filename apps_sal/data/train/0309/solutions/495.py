class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        h = dict()
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[j] - A[i]
                h.setdefault((j, diff), 1)
                h[i, diff] = h[j, diff] + 1
                res = max(res, h[i, diff])
        return res
