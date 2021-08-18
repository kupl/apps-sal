class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        keep = (A[0], 0)
        for j in range(1, len(A)):
            res = max(res, keep[0] + A[j] + keep[1] - j)
            if A[j] >= keep[0] or keep[0] - A[j] < j - keep[1]:
                keep = (A[j], j)
        return res
