class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        tmp_sum = sum(A[:L])
        i = L
        L_sum = [tmp_sum]
        while i < len(A):
            tmp_sum -= A[i - L]
            tmp_sum += A[i]
            L_sum.append(tmp_sum)
            i += 1
        tmp_sum = sum(A[:M])
        i = M
        M_sum = [tmp_sum]
        while i < len(A):
            tmp_sum -= A[i - M]
            tmp_sum += A[i]
            M_sum.append(tmp_sum)
            i += 1
        max_sum = 0
        for (i, lsum) in enumerate(L_sum):
            for j in range(i + L, len(M_sum)):
                max_sum = max(max_sum, lsum + M_sum[j])
        for (i, msum) in enumerate(M_sum):
            for j in range(i + M, len(L_sum)):
                max_sum = max(max_sum, msum + L_sum[j])
        return max_sum
