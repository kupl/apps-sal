class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        curr_max = A[0]
        max_sum = A[0]

        curr_min = A[0]
        min_sum = A[0]

        for i in range(1, len(A)):

            curr_max = max(A[i], A[i] + curr_max)
            max_sum = max(curr_max, max_sum)

            curr_min = min(A[i], A[i] + curr_min)
            min_sum = min(curr_min, min_sum)

        if max_sum > 0:
            return max(sum(A) - min_sum, max_sum)
        else:
            return max(A)
