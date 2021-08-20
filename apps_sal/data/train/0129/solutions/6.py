class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = float('-inf')
        if len(A) < 2:
            return 0
        one = A[0]
        for i in range(1, len(A)):
            ans = max(ans, one + A[i] - i)
            one = max(one, A[i] + i)
        return ans
