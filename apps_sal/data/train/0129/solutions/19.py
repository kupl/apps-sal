class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        preMax = A[0]
        ans = 0
        for i, a in enumerate(A[1:], 1):
            ans = max(ans, a - i + preMax)
            preMax = max(preMax, a + i)
        return ans
