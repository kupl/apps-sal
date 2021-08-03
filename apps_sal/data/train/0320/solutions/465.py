from functools import lru_cache


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        res = 0

        @lru_cache(None)
        def dp(n):
            if n == 0:
                return (0, 0)
            else:
                add, mul = 0, 0
                if n & 1 == 1:
                    a, b = dp(n - 1)
                    return (a + 1, b)
                else:
                    a, b = dp(n // 2)
                    return (a, b + 1)
        res = 0
        m = 0
        for i in nums:
            a, b = dp(i)
            res += a
            m = max(m, b)
        return res + m
