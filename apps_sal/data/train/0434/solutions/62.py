class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        zeros = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r - l)
            r += 1
        return res
