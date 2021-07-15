class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
#         total, maxSum, curMax, minSum, curMin = 0, float('-inf'), 0, float('inf'), 0
        
#         for a in A:
#             curMax = max(curMax + a, a)
#             maxSum = max(maxSum, curMax)
#             curMin = min(curMin + a, a)
#             minSum = min(minSum, curMin)
#             total += a
            
#         return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    
    
        if not A:
            return 0
        
        dp_max = [-99999] * len(A)
        dp_min = [-99999] * len(A)
        dp_max[0], dp_min[0] = A[0], A[0]
        
        for i in range(1, len(A)):
            dp_max[i] = max(A[i], dp_max[i - 1] + A[i])
            dp_min[i] = min(A[i], dp_min[i - 1] + A[i])
        
        if min(dp_min) == sum(A):
            return max(dp_max)
        else:
            return max(max(dp_max), sum(A) - min(dp_min))
