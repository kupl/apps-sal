class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        M_sum_greater_than = [0] * len(A)
        M_sum_smaller_than = [0] * len(A)

        prefix_sum = [A[0]]
        for n in A[1:]:
            prefix_sum.append(prefix_sum[-1] + n)

        for i in range(M - 1, len(A)):
            if i < M:
                M_sum_smaller_than[i] = max(M_sum_smaller_than[i - 1], prefix_sum[i])
            else:
                M_sum_smaller_than[i] = max(M_sum_smaller_than[i - 1], prefix_sum[i] - prefix_sum[i - M])

        for j in range(len(A) - M, -1, -1):
            if j == 0:
                M_sum_greater_than[j] = max(M_sum_greater_than[j + 1], prefix_sum[j + M - 1])
            else:
                M_sum_greater_than[j] = max(M_sum_greater_than[min(j + 1, len(A) - 1)], prefix_sum[j + M - 1] - prefix_sum[j - 1])

        max_sum = 0
        for start in range(len(A) - L + 1):
            if start == 0:
                sum_L = prefix_sum[start + L - 1]
            else:
                sum_L = prefix_sum[start + L - 1] - prefix_sum[start - 1]

            if start - 1 >= M - 1:
                max_sum = max(max_sum, sum_L + M_sum_smaller_than[start - 1])
            if start + L <= len(A) - M:
                max_sum = max(max_sum, sum_L + M_sum_greater_than[start + L])

        return max_sum
