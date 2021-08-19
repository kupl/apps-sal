class Solution:

    def maxSubarrayOfLengthK(self, A, start, end, K):
        if end - start < K:
            return (float('-inf'), 0, len(A) + 1)
        total_sum = 0
        for i in range(start, start + K):
            total_sum += A[i]
        opt_sum = (total_sum, start, start + K - 1)
        for j in range(start + K, end):
            total_sum += A[j] - A[j - K]
            if total_sum > opt_sum[0]:
                opt_sum = (total_sum, j - K + 1, j)
        return opt_sum

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sums = [0 for _ in A + [0]]
        for i in range(1, len(A) + 1):
            prefix_sums[i] = A[i - 1] + prefix_sums[i - 1]

        def solve(prefix_sums, L, M):
            res = 0
            for i in range(len(A) - L):
                total_sum = prefix_sums[i + L] - prefix_sums[i]
                (l1, r1) = (0, i)
                (l2, r2) = (i + L, len(A))
                other = max(self.maxSubarrayOfLengthK(A, l1, r1, M)[0], self.maxSubarrayOfLengthK(A, l2, r2, M)[0])
                res = max(total_sum + other, res)
            return res
        return max(solve(prefix_sums, L, M), solve(prefix_sums, M, L))
