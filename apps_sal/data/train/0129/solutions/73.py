class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        import sys
        val = A[0] + 0
        ans = -sys.maxsize
        A.pop(0)
        for i, num in enumerate(A):
            ans = max(ans, val + A[i] - i - 1)
            val = max(val, A[i] + i + 1)
        return ans
