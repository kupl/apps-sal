class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        m = -float('inf')
        res = -float('inf')
        for i in range(len(A) - 1, -1, -1):
            res = max(res, A[i] + i + m)
            m = max(m, A[i] - i)
        return res
