class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # naive will be n^2: try every possible start position

        # 3 cases

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
        if minimum == 0:  # means the entire araay is negative, so we take the max element
            return maximum
        return max(maximum, minimum)

        # take the max of 3 cases
        # 1. maximum
        # 2. total - minimum
        # 3. if all negatives, then the max should be the maximum

        # [-2,-3,-1]. Take a look at this case, for example.
