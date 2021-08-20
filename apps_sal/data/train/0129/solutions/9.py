class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = imax = 0
        for (i, a) in enumerate(A):
            res = max(res, imax + A[i] - i)
            imax = max(imax, A[i] + i)
        return res
