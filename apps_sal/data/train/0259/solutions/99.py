import math

def divide_and_sum(nums, divisor):
    return sum([math.ceil(x / divisor) for x in nums])

class Solution:
    def smallestDivisor(self, nums, threshold):
        start = max(nums)
        end = 1

        assert divide_and_sum(nums, start) <= threshold, 'impossible, threshold is guaranteed to be at least len(nums)'
        if divide_and_sum(nums, end) <= threshold:
            # there are no divisors smaller than 1
            return end

        # loop invariant:
        # dsum(nums, start) <= threshold
        # dsum(nums, end)   >= threshold
        while start >= end:
            mid = (start + end) // 2
            dsum = divide_and_sum(nums, mid)
            if dsum == threshold:
                #print('case 1')
                mid -= 1
                while divide_and_sum(nums, mid) == threshold:
                    mid -= 1
                return mid + 1
            if dsum > threshold:
                # divisor is too small
                end = mid + 1
            if dsum < threshold:
                # threshold is too large
                start = mid - 1
        #print('case 2')
        #loop exit condition:
        #start < end
        #dsum(nums, start) <= threshold
        #dsum(nums, end)   >= threshold
        print((start, end, divide_and_sum(nums, start), divide_and_sum(nums, end)))
        return end

