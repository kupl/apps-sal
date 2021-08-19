class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M > len(A):
            return 0
        max_end = [0 for i in range(len(A))]
        max_start = [0 for i in range(len(A))]

        def max_sum(L, M):
            (sum1, sum2, max_sum1, max_sum2, max_sum) = (0, 0, 0, 0, 0)
            for i in range(len(A)):
                max_sum2 = max(sum2, max_sum2)
                max_start[len(A) - i - 1] = max_sum2
                if i >= L:
                    sum1 -= A[i - L]
                if i >= M:
                    sum2 -= A[len(A) - i + M - 1]
                sum1 += A[i]
                sum2 += A[len(A) - 1 - i]
                max_sum1 = max(sum1, max_sum1)
                max_end[i] = max_sum1
            for i in range(L - 1, len(A) - M):
                max_sum = max(max_sum, max_end[i] + max_start[i])
            return max_sum
        return max(max_sum(L, M), max_sum(M, L))
