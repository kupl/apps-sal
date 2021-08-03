from functools import lru_cache


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)

        @lru_cache(None)
        def dp(l, r):
            if r - l <= 1:
                return 0
            return min(max(arr[l:m]) * max(arr[m:r]) + dp(l, m) + dp(m, r) for m in range(l + 1, r))

        return dp(0, N)
