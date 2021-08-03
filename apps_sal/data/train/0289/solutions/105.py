from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L0: int, M0: int) -> int:
        def range_sum(i, j):
            return accum[j - 1] - (accum[i - 1] if i > 0 else 0)
        if not A:
            return 0
        max_sum = 0
        accum = list(accumulate(A, lambda x, y: x + y))
        for L, M in ((L0, M0), (M0, L0)):
            for i in range(len(A) - L + 1):
                sum1 = range_sum(i, i + L)
                for j in range(i + L, len(A) - M + 1):
                    sum2 = range_sum(j, j + M)
                    max_sum = max(max_sum, sum1 + sum2)
        return max_sum
