class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        tot = sum(A)
        B = A[:]
        
        for i in range(1, len(A)):
            if A[i - 1] > 0:
                A[i] += A[i - 1]
            if B[i - 1] < 0:
                B[i] += B[i - 1]
        
        submax = max(A)
        submin = min(B)
        
        return max(submax, tot - submin) if tot != submin else submax
            

