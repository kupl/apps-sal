class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @lru_cache(None)
        def dp(n, k):
            if n < k:
                return 0
            if k == 1:
                return sum(A[:n]) / n
            cur, ans = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                ans = max(ans, dp(i, k - 1) + cur / (n - i))
            return ans
        return dp(len(A), K)
