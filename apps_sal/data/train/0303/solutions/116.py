class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i):
            ans = 0
            for k in range(K):
                if i - k >= 0:
                    ans = max(ans, max(A[i - k:i + 1]) * (k + 1) + dp(i - k - 1))
            return ans
        return dp(len(A) - 1)
