from functools import lru_cache


class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        l = len(A)

        @lru_cache(None)
        def dp(n, k):
            if n < k:
                return 0
            if k == 1:
                return sum(A[:n]) / float(n)
            (cur, ans) = (0, 0)
            for i in range(n - 1, 0, -1):
                cur += A[i]
                ans = max(ans, dp(i, k - 1) + cur / float(n - i))
            return ans
        return dp(l, K)
