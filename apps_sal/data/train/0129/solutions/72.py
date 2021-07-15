class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if len(A) <= 1:
            return -float('inf')

        candidate = max(A[0], A[1]+1)
        res = A[0]+A[1]-1 

        for i in range(2, len(A)):
            res = max(res, candidate+A[i]-i)
            candidate = max(candidate, A[i]+i)
        return res            
