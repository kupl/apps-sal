import functools
import sys


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sys.setrecursionlimit(10**6)

        @functools.lru_cache(None)
        def cal(n):
            if n == 0:
                return 0, 0
            if n % 2 == 0:
                a, b = cal(n // 2)
                return a, b + 1
            else:
                a, b = cal(n - 1)
                return a + 1, b
            return a, b
        ans = 0
        mul = 0
        for e in nums:
            a, b = cal(e)
            ans += a
            mul = max(mul, b)
        #print(ans, mul)
        return ans + mul
