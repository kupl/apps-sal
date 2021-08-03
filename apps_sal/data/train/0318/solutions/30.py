class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        N = len(slices)

        @lru_cache(None)
        def dp(i, k, d):
            if 3 * k == N:
                return 0
            if i >= N - d:
                return -math.inf
            return max(slices[i] + dp(i + 2, k + 1, d), dp(i + 1, k, d))

        return max(slices[0] + dp(2, 1, 1), dp(1, 0, 0))
