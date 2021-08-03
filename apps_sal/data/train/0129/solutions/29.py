class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        d = 0
        m = A[0]
        for i in range(1, len(A)):
            d = max(d, A[i - 1] + (i - 1))
            m = max(A[i] - i + d, m)
        return m
