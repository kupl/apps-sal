class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        lmax = A[0]
        gmax = float('-inf')
        for i in range(1, len(A)):
            cur = lmax + A[i] - i
            lmax = max(lmax, A[i] + i)
            gmax = max(gmax, cur)
        return gmax
