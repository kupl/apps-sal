class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        point = (A[0], 0)
        best_val = A[0]
        best_ind = 0
        max_score = 0
        for ind in range(1, len(A)):
            max_score = max(max_score, best_val + A[ind] + best_ind - ind)
            if A[ind] + ind - best_ind >= best_val:
                best_val = A[ind]
                best_ind = ind
        return max_score
