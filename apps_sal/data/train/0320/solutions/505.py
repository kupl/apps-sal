class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def check(num):
            divisions = inc = 0
            while num:
                if num % 2:
                    inc += 1
                divisions += 1
                num //= 2
            return (divisions, inc)
        res = 0
        m = 1
        for n in nums:
            (d, r) = check(n)
            m = max(m, d)
            res += r
        return res + m - 1
