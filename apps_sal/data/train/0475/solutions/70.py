class Solution:
    def rangeSum(self, A, n, left, right):
        B, C = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + A[i]
            C[i + 1] = C[i] + B[i + 1]

        def count_sum_under(score):
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += j - i
            return res

        def sum_k_sums(k):
            score = kth_score(k)
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += B[j] * (j - i + 1) - (C[j] - (C[i - 1] if i else 0))
            return res - (count_sum_under(score) - k) * score

        def kth_score(k):
            l, r = 0, B[n]
            while l < r:
                m = (l + r) // 2
                if count_sum_under(m) < k:
                    l = m + 1
                else:
                    r = m
            return l

        return (sum_k_sums(right) - sum_k_sums(left - 1)) % (10 ** 9 + 7)
