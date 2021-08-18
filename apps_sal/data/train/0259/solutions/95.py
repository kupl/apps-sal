import math


def divide_and_sum(nums, divisor):
    return sum([math.ceil(x / divisor) for x in nums])


class Solution:
    def smallestDivisor(self, nums, threshold):
        start = max(nums)
        end = 1

        assert divide_and_sum(nums, start) <= threshold, 'impossible, threshold is guaranteed to be at least len(nums)'
        if divide_and_sum(nums, end) <= threshold:
            return end

        while start >= end:
            mid = (start + end) // 2
            dsum = divide_and_sum(nums, mid)
            if dsum == threshold:
                while divide_and_sum(nums, mid) == threshold:
                    mid -= 1
                return mid + 1
            if dsum > threshold:
                end = mid + 1
            if dsum < threshold:
                start = mid - 1
        return end
