class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        (lag, lead) = (0, 1)
        prev_max_score = A[0]
        prev_max_idx = 0
        max_score = 0
        for i in range(1, len(A)):
            score = prev_max_score + A[i] - (i - prev_max_idx)
            max_score = max(score, max_score)
            if A[i] >= score - A[i]:
                prev_max_idx = i
                prev_max_score = A[i]
        return max_score
