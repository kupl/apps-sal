class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 1. get max subarray sum
        maxSum = curSum = A[0]
        for i in range(1, len(A)):
            curSum = max(A[i], A[i] + curSum)
            maxSum = max(maxSum, curSum)

        if maxSum < 0:
            return maxSum

        # 2. get min subarray sum
        minSum = curSum = A[0]
        for i in range(1, len(A)):
            curSum = min(A[i], A[i] + curSum)
            minSum = min(minSum, curSum)

        # 3. compare (max subarray sum) with (total sum - min subarray sum)
        return max(sum(A) - minSum, maxSum)
