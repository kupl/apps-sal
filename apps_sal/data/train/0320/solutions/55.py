class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        s = sum(nums)
        while (s):
            odd_ct = len([0 for n in nums if (n & 1)])
            op += odd_ct
            s -= odd_ct
            if s != 0:
                nums = [n // 2 for n in nums]
                op += 1
                s /= 2
        return op
