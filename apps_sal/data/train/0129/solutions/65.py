class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        m = p = 0
        for (i, n) in enumerate(A):
            m = max(m, p + n - i)
            p = max(p, n + i)
        return m
