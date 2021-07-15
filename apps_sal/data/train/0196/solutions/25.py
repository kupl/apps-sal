class Solution:
    def maxSubarraySumCircular1(self, A: List[int]) -> int:
        maxSubarraySum = [i for i in A]
        minSubarraySum = [i for i in A]
        for i in range(1,len(A)):
            maxSubarraySum[i] = max(maxSubarraySum[i-1]+A[i],A[i])
        for i in range(1,len(A)):
            minSubarraySum[i] = min(minSubarraySum[i-1]+A[i],A[i])
        return max(max(maxSubarraySum),sum(A)-min(minSubarraySum)) if max(maxSubarraySum) >0 else max(maxSubarraySum)
    
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
