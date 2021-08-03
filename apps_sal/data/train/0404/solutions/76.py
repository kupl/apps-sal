class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return float('-inf')
            if j == 1:
                return sum(A[i:]) / (n - i)
            ans = float('-inf')
            cur_sum = 0
            for l in range(i, n):
                cur_sum += A[l]
                ans = max(ans, cur_sum / (l - i + 1) + dp(l + 1, j - 1))
            return ans
        return dp(0, K)
