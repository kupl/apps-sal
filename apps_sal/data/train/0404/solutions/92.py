from functools import lru_cache


class Solution(object):
    def largestSumOfAverages(self, A, K):
        l = len(A)
        revsum = [0] * (l - 1) + [A[-1]]
        for i in range(l - 1)[::-1]:
            revsum[i] = revsum[i + 1] + A[i]
        # print(revsum)

        @lru_cache(None)
        def dp(n, k):
            if n < k:
                return 0
            if k == 1:
                return sum(A[:n]) / float(n)
            cur, ans = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                ans = max(ans, dp(i, k - 1) + (revsum[i] - (revsum[n] if n != l else 0)) / float(n - i))
            return ans
        return dp(l, K)
