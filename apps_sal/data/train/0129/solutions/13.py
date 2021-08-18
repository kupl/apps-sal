class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_i = 0
        score_max_i_j = []
        for j in range(len(A)):
            score_max_i_j.append(max_i + A[j] - j)
            max_i = max(max_i, A[j] + j)
        return max(score_max_i_j)
