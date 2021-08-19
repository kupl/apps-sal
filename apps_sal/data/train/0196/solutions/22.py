class Solution:

    def maxSubarraySumCircular1(self, A: List[int]) -> int:
        maxSubarraySum = [i for i in A]
        minSubarraySum = [i for i in A]
        for i in range(1, len(A)):
            maxSubarraySum[i] = max(maxSubarraySum[i - 1] + A[i], A[i])
        for i in range(1, len(A)):
            minSubarraySum[i] = min(minSubarraySum[i - 1] + A[i], A[i])
        return max(max(maxSubarraySum), sum(A) - min(minSubarraySum)) if max(maxSubarraySum) > 0 else max(maxSubarraySum)

    def maxSubarraySumCircular(self, A):
        total = 0
        curMax = 0
        maxSubArraySum = A[0]
        curMin = 0
        minSubArraySum = A[0]
        for a in A:
            curMax = max(curMax + a, a)
            maxSubArraySum = max(maxSubArraySum, curMax)
            curMin = min(curMin + a, a)
            minSubArraySum = min(minSubArraySum, curMin)
            total += a
        return max(maxSubArraySum, total - minSubArraySum) if maxSubArraySum > 0 else maxSubArraySum
