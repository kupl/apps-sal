from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i, k, p, l):
            if k < 0:
                return sys.maxsize // 2
            if i >= len(s):
                return 0

            if s[i] == p:
                carry = l in [1, 9, 99]
                return carry + dp(i + 1, k, p, l + 1)
            else:
                return min(dp(i + 1, k - 1, p, l),
                           1 + dp(i + 1, k, s[i], 1))
        return dp(0, k, '', 0)
