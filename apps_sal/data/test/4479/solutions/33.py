class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        if not A: return sum(A)
        
        if K == 0: return sum(A)
        
        
        for i in range(K):
    
            A[A.index(min(A))] = - A[A.index(min(A))]
        
        return sum(A)
