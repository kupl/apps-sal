import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums
        self.threshold = threshold
        num_sum = sum(nums)
        l = math.floor(num_sum / threshold) - 1
        h = num_sum
        m = math.ceil((l + h) / 2)
        while h != m:
            if self.validate_divisor(m):
                h = m
            else:
                l = m
            m = math.ceil((l + h) / 2)
        return h

    def validate_divisor(self, divisor):
        if divisor <= 0:
            return False
        s = sum(math.ceil(x / divisor) for x in self.nums)
        return s <= self.threshold
