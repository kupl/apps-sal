class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = maxx = 0
        for i in range(len(A)):
            res = max(res, maxx + A[i])
            maxx = max(maxx, A[i]) - 1
        return res
