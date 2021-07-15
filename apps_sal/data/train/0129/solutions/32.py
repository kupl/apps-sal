class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        res = max_i = -n
        for j in range(1,n):
            max_i = max(max_i, A[j-1] + j-1)
            res = max(res, max_i + A[j] - j)
        return res
        

