from operator import itemgetter


class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        B = [(i, A[i]) for i in range(0, len(A))]
        B.sort(key=itemgetter(1))
        curminidx = B[0][0]
        res = 0
        for i in range(1, len(A)):
            curidx = B[i][0]
            if curidx < curminidx:
                curminidx = curidx
            else:
                res = max(res, curidx - curminidx)
        return res
