class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        K = A[0]
        best = float('-inf')
        for j in range(1, len(A)):
            x = A[j]
            best = max(best, K + x - j)
            K = max(K, x + j)
        return best
