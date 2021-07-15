class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxI = A[0]
        ans = A[0] + A[1] - 1
        for i in range(1, len(A)):
            if ans < maxI + A[i] - i:
                ans = maxI + A[i] - i
            if maxI < A[i] + i:
                maxI = A[i] + i
        return ans
