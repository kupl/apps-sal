from functools import lru_cache


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, k, last, cnt):
            if k < 0:
                return float('inf')
            if i + k >= n:
                return 0
            res = n
            if last == s[i]:
                carry = int(cnt == 1 or cnt == 9 or cnt == 99)
                res = min(res, dp(i + 1, k, last, cnt + 1) + carry)
            else:
                res = min(res, dp(i + 1, k, s[i], 1) + 1, dp(i + 1, k - 1, last, cnt))
            return res
        return dp(0, k, '', 0)
