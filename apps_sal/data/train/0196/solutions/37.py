class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        minSum = A[0]
        maxSum = A[0]
        maximum = A[0]
        minimum = A[0]
        for i in range(1, len(A)):
            if A[i] > maxSum + A[i]:
                maxSum = A[i]
            else:
                maxSum += A[i]
            maximum = max(maximum, maxSum)
            if A[i] < minSum + A[i]:
                minSum = A[i]
            else:
                minSum += A[i]
            minimum = min(minimum, minSum)
        minimum = sum(A) - minimum
        if minimum == 0:
            return maximum
        return max(maximum, minimum)
