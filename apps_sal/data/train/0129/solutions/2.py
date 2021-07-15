class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        m = A[0]
        
        for j in range(1, len(A)):
            res = max(res, A[j] - j + m)
            m = max(m, A[j] + j)
        
        return res

