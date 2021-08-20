class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        maxI = A[0] + 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, maxI + A[j] - j)
            maxI = max(maxI, A[j] + j)
        return res
