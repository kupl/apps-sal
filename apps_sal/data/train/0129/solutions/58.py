class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:

        # generate a vector
        A_left = [a + i for i, a in enumerate(A)]
        A_right = [a - i for i, a in enumerate(A)]
        _max_left = A_left[0]
        _max = 0
        for j in range(1, len(A_right)):
            _max = max(_max_left + A_right[j], _max)
            _max_left = max(_max_left, A_left[j])
        return _max
