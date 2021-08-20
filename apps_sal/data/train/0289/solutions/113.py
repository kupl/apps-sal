class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        sum_l = [sum(A[i:i + L]) for i in range(N - L + 1)]
        sum_m = [sum(A[i:i + M]) for i in range(N - M + 1)]
        max_sum = 0
        for i in range(len(sum_l)):
            for j in range(len(sum_m)):
                if i <= j and j < i + L or (i >= j and i < j + M):
                    continue
                max_sum = max(max_sum, sum_l[i] + sum_m[j])
        return max_sum
