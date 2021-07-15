class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        n = len(A)
        m = A[0]
        j = 0
        for i in range(1, n):
            res = max(res, (A[i]+A[j]+j-i))
            if A[i]+i-j > m:
                m = A[i]
                j = i
        return res
