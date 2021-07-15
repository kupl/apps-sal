class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # find linear max subarray sum
        maxSum = A[0]
        curMaxSum = A[0]
        for i in range(1, len(A)):
            curMaxSum = max(curMaxSum + A[i], A[i])
            maxSum = max(maxSum, curMaxSum)
        
        # find linear min subarray sum
        minSum = A[0]
        curMinSum = A[0]
        for i in range(1, len(A)):
            curMinSum = min(curMinSum + A[i], A[i])
            minSum = min(minSum, curMinSum)
        
        # edge case: all values of A are negative
        if maxSum < 0:
            return maxSum
        
        # compare (linear max) with (total sum - linear min)
        return max(maxSum, sum(A)-minSum)

