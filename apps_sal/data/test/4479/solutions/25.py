class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        while K > 0:
            min_index = A.index(min(A))
            A[min_index] = - A[min_index]
            K = K - 1
        
        return sum(A)

