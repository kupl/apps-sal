class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M == len(A):
            return sum(A)

        max_sum2 = 0
        cur_sum2 = 0
        total_len = len(A)

        def find_max_subarray(start_idx, end_idx, l):

            nonlocal A
            max_sum = 0
            cur_sum = 0
            for idx in range(start_idx, l + start_idx):
                max_sum += A[idx]
            cur_sum = max_sum

            for idx in range(l + start_idx, end_idx):
                cur_sum = cur_sum + A[idx] - A[idx - l]
                max_sum = max(max_sum, cur_sum)
            return max_sum

        cur_sum2 = 0
        for idx in range(L):
            cur_sum2 += A[idx]

        max_sum2 = cur_sum2 + find_max_subarray(L, total_len, M)

        for idx in range(L, total_len - M):
            cur_sum2 = cur_sum2 + A[idx] - A[idx - L]
            max_sum2 = max(max_sum2, cur_sum2 + find_max_subarray(idx + 1, total_len, M))

        if L != M:
            cur_sum2 = 0
            for idx in range(M):
                cur_sum2 += A[idx]
            max_sum2 = max(max_sum2, cur_sum2 + find_max_subarray(M, total_len, L))
            for idx in range(M, total_len - L):
                cur_sum2 = cur_sum2 + A[idx] - A[idx - M]
                max_sum2 = max(max_sum2, cur_sum2 + find_max_subarray(idx + 1, total_len, L))

        return max_sum2
