class Solution:
    import math

    def minOperations(self, nums: List[int]) -> int:

        def f(s):
            n = 0
            p = 0
            while s:
                if s % 2 == 0:
                    s = s // 2
                    p += 1
                else:
                    s -= 1
                n += 1
            return (n, p)
        nums.sort(key=lambda x: f(x)[1])
        res = 0
        inc = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                (n, p) = f(nums[i])
                res += n - p
                res += p - inc
                inc = p
        return res
