class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sum = [0] * (len(A) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = A[i - 1] + prefix_sum[i - 1]
        max_sum = 0
        for i in range(L, len(prefix_sum)):
            L_sum = prefix_sum[i] - prefix_sum[i - L]
            for j in range(i + M, len(prefix_sum)):
                M_sum = prefix_sum[j] - prefix_sum[j - M]
                max_sum = max(max_sum, L_sum + M_sum)
        for i in range(M, len(prefix_sum)):
            M_sum = prefix_sum[i] - prefix_sum[i - M]
            for j in range(i + L, len(prefix_sum)):
                L_sum = prefix_sum[j] - prefix_sum[j - L]
                max_sum = max(max_sum, L_sum + M_sum)
        return max_sum
