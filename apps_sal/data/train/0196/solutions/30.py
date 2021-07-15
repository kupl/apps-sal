class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Maximum Sum Circular Subarray
        # 8/22/20 3:41
        total, maxSum = 0, A[0]
        curMax, minSum, curMin = 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if total != minSum else maxSum
    
    

# input: [5,-3,5]
# Output:7
# Expected:10

                    
                
            
            
         

