class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        for i in range(K) :
            check = min(A)
            t = A.index(check)
            A[t] = -A[t]
        
        return sum(A)
            
        
        
        
        

