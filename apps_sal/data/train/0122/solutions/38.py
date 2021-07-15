class Solution:
    def maxScore(self, A: List[int], k: int) -> int:    
        su = sum(A[:k])
        n = len(A) 
        res = su   
        for i in range(k):
            su -= A[k-i-1]
            su += A[n-i-1]
            res = max(res, su) 
        return res
