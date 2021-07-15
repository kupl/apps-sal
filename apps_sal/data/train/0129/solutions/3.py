class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = -math.inf
        best = -math.inf
        for i,a in enumerate(A):
            ans = max(ans, best + a - i)
            best = max(best, a + i)
        
        return ans
