class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        d = A[1] + A[0] - 1
        m = A[0]
        for j in range(1, len(A)):
            if m + A[j] - j > d:
                d = m + A[j] - j
            if A[j] + j >= m:
                m = A[j] + j
        return d
