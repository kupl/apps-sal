class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        best = A[0] - 1
        for i in range(1, len(A)):
            ans = max(ans, A[i] + best)
            best = max(best - 1, A[i] - 1)
        return ans
