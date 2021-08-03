class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # case 1, kadane's algo
        totalSum = sum(A)
        curr = A[0]
        maxSum = A[0]

        for i in range(1, len(A)):
            if A[i] + curr > A[i]:
                curr = A[i] + curr
            else:
                curr = A[i]

            maxSum = max(maxSum, curr)

        # case 2, wrapping

        curr = A[0]
        minSum = totalSum

        for i in range(1, len(A)):
            curr = min(A[i] + curr, A[i])

            minSum = min(minSum, curr)

        if totalSum == minSum:
            return maxSum
        return max(totalSum - minSum, maxSum)
