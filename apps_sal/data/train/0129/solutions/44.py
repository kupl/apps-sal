class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if len(A) <= 1:
            return 0
        max_A_plus_i = max(A[0], A[1] + 1)
        max_score = A[0] + A[1] - 1
        for i in range(2, len(A)):
            max_score = max(max_score, max_A_plus_i + A[i] - i)
            max_A_plus_i = max(max_A_plus_i, A[i] + i)

        return max_score
