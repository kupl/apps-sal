class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        res = A[0]
        cur = A[0]
        sumn = sum(A)
        for num in A[1:]:
            cur = num + max(0, cur)
            res = max(cur, res)
        if len(A) >= 2:
            mincur = -A[1]
            minres = -A[1]
            for num in A[2:]:
                mincur = -num + max(0, mincur)
                minres = max(minres, mincur)
            res = max(res, sumn + minres)
            mincur = -A[0]
            minres = -A[0]
            for num in A[1:len(A) - 1]:
                mincur = -num + max(0, mincur)
                minres = max(minres, mincur)
            res = max(res, sumn + minres)
        return res
