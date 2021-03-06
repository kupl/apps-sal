class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        _max_left = A[0]
        _max = 0
        for j in range(1, len(A)):
            _max = max(_max_left + A[j] - j, _max)
            _max_left = max(_max_left, A[j] + j)
        return _max
