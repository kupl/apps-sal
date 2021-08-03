class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if len(A) < 2:
            return -1

        best_so_far = A[0] + 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, best_so_far + A[j] - j)
            if best_so_far < A[j] + j:
                best_so_far = A[j] + j

        return res
