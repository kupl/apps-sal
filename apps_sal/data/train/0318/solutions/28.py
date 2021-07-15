class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, remaining, version):
            if i > len(slices) - version:
                return 0
            if remaining == 0:
                return 0
            else:
                return max(dp(i + 1, remaining, version), slices[i] + dp(i + 2, remaining - 1, version))
        return max(dp(1, len(slices) // 3, 1), dp(0, len(slices) // 3, 2))
