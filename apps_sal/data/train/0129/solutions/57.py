class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        prev = ans = float('-inf')
        for i in range(1, len(A)):
            prev = max(prev, A[i - 1] + i - 1)
            ans = max(ans, prev + A[i] - i)
        return ans
