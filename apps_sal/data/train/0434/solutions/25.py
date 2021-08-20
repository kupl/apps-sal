class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        start = end = zeros = ones = maxx = 0
        while end < len(nums):
            if nums[end] == 0:
                zeros += 1
            else:
                ones += 1
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            maxx = max(maxx, end - start)
            end += 1
        return maxx
