class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        L = len(A)
        cum_sum = [0] * L
        cum_max = [0] * L
        cum_max_final = [0] * L
        sum_ = 0
        for i in range(L):
            sum_ += A[i]
            cum_sum[i] = sum_
            if i == 0:
                cum_max[i] = A[i]
            else:
                if cum_max[i - 1] > 0:
                    cum_max[i] = cum_max[i - 1] + A[i]
                else:
                    cum_max[i] = A[i]
        m = A[L - 1]
        for i in range(L - 1, -1, -1):
            if i != 0:
                cur = cum_sum[L - 1] - cum_sum[i - 1]
                cum_max_final[i] = max(cur, m)
                m = max(m, cur)

            else:
                cum_max_final[i] = max(m, cum_sum[L - 1])

        res = -float('inf')
        for i in range(L):
            if i != L - 1:
                cur = cum_max[i]
                cur = max(cur, cum_sum[i] + cum_max_final[i + 1])
                res = max(res, cur)
            else:
                res = max(res, cum_max[L - 1])
        return res
