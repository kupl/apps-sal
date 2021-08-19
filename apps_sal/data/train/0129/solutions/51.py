class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        N = len(A)
        max_ = 0
        prev = A[-1] - N + 1
        for i in range(N - 2, -1, -1):
            max_ = max(max_, prev + A[i] + i)
            prev = max(prev, A[i] - i)
        return max_
