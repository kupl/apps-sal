class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        idx = min(range(n), key=lambda x: slices[x])
        slices = slices[idx + 1:] + slices[:idx]

        @lru_cache(None)
        def dp(i, k):
            if i >= n - 1 or k == 0:
                return 0
            return max(slices[i] + dp(i + 2, k - 1), dp(i + 1, k))
        return dp(0, n // 3)
