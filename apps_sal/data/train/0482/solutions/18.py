class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def cached_max(i, j):
            return max(arr[i: j] or [1])

        @lru_cache(None)
        def dp(i, j):
            if j - i <= 1:
                return 0
            elif j - i == 2:
                return arr[i] * arr[i + 1]
            return min(dp(i, k) + dp(k, j) + cached_max(i, k) * cached_max(k, j)
                       for k in range(i + 1, j))

        return dp(0, len(arr))
