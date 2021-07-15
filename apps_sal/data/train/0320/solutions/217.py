from functools import lru_cache
class Solution:
    def minOperations(self, nums) -> int:
        @lru_cache(None)
        def minOpt(num):
            if num == 0:
                return 0, 0
            if num % 2 == 1:
                m, a = minOpt(num -1)
                return m, a + 1
            else:
                m, a = minOpt(num //2 )
                return m + 1, a

        multiply, add = 0, 0
        for num in nums:
            m, a = minOpt(num)
            multiply = max(m, multiply)
            add += a
        return multiply + add
