class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = imax = 0
        for (i, a) in enumerate(A):
            res = max(res, imax + a - i)
            imax = max(imax, a + i)
        return res
