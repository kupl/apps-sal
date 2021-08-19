class Solution:
    def rangeSum(self, A, n, left, right):
        # B: partial sum of A
        # C: partial sum of B
        # Use prefix sum to precompute B and C
        B, C = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + A[i]
            C[i + 1] = C[i] + B[i + 1]

        # Use two pointer to
        # calculate the total number of cases if B[j] - B[i] <= score
        def count_sum_under(score):
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += j - i
            return res

        # calculate the sum for all numbers whose indices are <= index k
        def sum_k_sums(k):
            score = kth_score(k)
            res = i = 0
            for j in range(n + 1):
                # Proceed until B[i] and B[j] are within score
                while B[j] - B[i] > score:
                    i += 1
                res += B[j] * (j - i + 1) - (C[j] - (C[i - 1] if i else 0))
            return res - (count_sum_under(score) - k) * score

        # use bisearch to find how many numbers ae below k
        def kth_score(k):
            l, r = 0, B[n]
            while l < r:
                m = (l + r) // 2
                if count_sum_under(m) < k:
                    l = m + 1
                else:
                    r = m
            return l

        # result between left and right can be converted to [0, right] - [0, left-1] (result below right - result below left-1)
        return (sum_k_sums(right) - sum_k_sums(left - 1)) % (10 ** 9 + 7)
