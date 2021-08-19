class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        dp = 0
        ans = 0
        for j in range(0, n):
            ans = max(ans, A[j] - j + dp)
            dp = max(dp, A[j] + j)
        return ans
