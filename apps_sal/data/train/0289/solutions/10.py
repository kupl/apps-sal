class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        NA = len(A)
        N1, N2 = max(L, M), min(L, M)
        sum_window = [[0] * NA for _ in range(2)]
        sum1 = sum2 = max_sum = 0
        for i, v in enumerate(A):
            if i >= N1:
                sum1 -= A[i - N1]
            if i >= N2:
                sum2 -= A[i - N2]
            sum1 += v
            sum2 += v
            sum_window[0][i] = sum1
            sum_window[1][i] = sum2

            if i >= N1:
                for j in range(i - N1 + 1):
                    max_sum = max(max_sum, sum_window[0][i] + sum_window[1][j])
                for j in range(i - N2 + 1):
                    max_sum = max(max_sum, sum_window[1][i] + sum_window[0][j])

        return max_sum
