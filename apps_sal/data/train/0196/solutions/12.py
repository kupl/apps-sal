class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        n = len(A)
        cur_sum = A[0]
        result1 = A[0]
        for i in range(1,n):
            cur_sum = max(A[i],cur_sum+A[i])
            result1 = max(cur_sum,result1)
        
        if n == 1: return result1
        
        cur_sum = A[1]
        result2 = A[1]
        for i in range(2,n-1):
            cur_sum = min(A[i],cur_sum+A[i])
            result2 = min(cur_sum, result2)
            
        return max(result1,sum(A)-result2)
