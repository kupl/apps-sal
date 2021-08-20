class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        max_num = 0
        for n in nums:
            max_num = max(max_num, n)
            while n > 0:
                n = n & n - 1
                ops += 1
        if max_num:
            ops -= 1
        while max_num > 0:
            max_num >>= 1
            ops += 1
        return ops
