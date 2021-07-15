class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                return 0
            elif i >= j:
                return -math.inf
            else:
                return max(
                    slices[i] + dp(i + 2, j, k - 1),
                    dp(i + 1, j, k)
                )

        n = len(slices)
        s = n // 3
        return max(
            dp(1, n, s),
            dp(0, n - 1, s)
        )
