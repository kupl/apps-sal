class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        maximum = A[0]
        for i in range(1, len(A)):
            cur = A[i] - i
            res = max(res, cur + maximum)
            maximum = max(maximum, A[i] + i)
        return res
