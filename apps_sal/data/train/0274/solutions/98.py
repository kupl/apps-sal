class Solution:

    def longestSubarray(self, nums, limit):
        _min = _max = nums[0]
        count = 0
        (res, start) = (1, 0)
        for right in range(len(nums)):
            if _min > nums[right]:
                _min = nums[right]
            if _max < nums[right]:
                _max = nums[right]
            if _max - _min <= limit:
                count += 1
                if res < count:
                    res = count
            else:
                _min = _max = nums[right]
                count = 1
                left = right - 1
                while left >= start and abs(_max - nums[left]) <= limit and (abs(_min - nums[left]) <= limit):
                    if _min > nums[left]:
                        _min = nums[left]
                    if _max < nums[left]:
                        _max = nums[left]
                    count += 1
                    left -= 1
                start = right + 1
        return res
