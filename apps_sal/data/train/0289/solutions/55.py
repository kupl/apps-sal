class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        seg_sum_l = []
        seg_sum_m = []
        cum_sum = [0]
        n = len(A)
        for (i, a) in enumerate(A):
            cum_sum.append(a + cum_sum[-1])
            if i >= L - 1:
                seg_sum_l.append(cum_sum[i + 1] - cum_sum[i - L + 1])
            else:
                seg_sum_l.append(-1)
            if i >= M - 1:
                seg_sum_m.append(cum_sum[i + 1] - cum_sum[i - M + 1])
            else:
                seg_sum_m.append(-1)
        max_sum = -1
        for i in range(L - 1, n):
            for j in range(M - 1, i - L):
                cur_sum = seg_sum_l[i] + seg_sum_m[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
            for j in range(i + M, n):
                cur_sum = seg_sum_l[i] + seg_sum_m[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
        return max_sum
