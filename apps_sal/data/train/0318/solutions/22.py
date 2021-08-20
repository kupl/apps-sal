class Solution:

    def maxSizeSlices(self, s: List[int]) -> int:
        ct = len(s) // 3

        @lru_cache(None)
        def f(l, r, n):
            if n == 0:
                return 0
            if l > r:
                return -1e+18
            if n == 1:
                return max(s[l:r + 1])
            return max(f(l + 1, r, n), s[l] + f(l + 2, r, n - 1))
        return max(f(1, len(s) - 1, ct), s[0] + f(2, len(s) - 2, ct - 1))
