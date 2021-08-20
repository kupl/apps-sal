class Solution:

    def maxSubarraySumCircular(self, A):
        total = sum(A)
        max_sum = [0 for i in range(len(A))]
        min_sum = [0 for i in range(len(A))]
        max_sum[0] = A[0]
        min_sum[0] = A[0]
        best_non_loop = max_sum[0]
        best_inverse_loop = min_sum[0]
        for i in range(1, len(A)):
            max_sum[i] = A[i] + max(max_sum[i - 1], 0)
            min_sum[i] = A[i] + min(min_sum[i - 1], 0)
            best_non_loop = max(best_non_loop, max_sum[i])
            best_inverse_loop = min(best_inverse_loop, min_sum[i])
        ret = max(best_non_loop, total - best_inverse_loop)
        if ret == 0:
            return max(A)
        return ret
