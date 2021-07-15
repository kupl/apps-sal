class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSubarraySum = [i for i in A]
        minSubarraySum = [i for i in A]
        for i in range(1,len(A)):
            maxSubarraySum[i] = max(maxSubarraySum[i-1]+A[i],A[i])
        for i in range(1,len(A)):
            minSubarraySum[i] = min(minSubarraySum[i-1]+A[i],A[i])
        return max(max(maxSubarraySum),sum(A)-min(minSubarraySum)) if max(maxSubarraySum) >0 else max(maxSubarraySum)
