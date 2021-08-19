class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        (prev, res, curr) = (0, 0, 0)
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                if i < len(nums) - 1 and nums[i + 1] != 0:
                    prev = curr
                else:
                    prev = 0
                curr = 0
            res = max(res, curr + prev)
        if res == len(nums):
            res -= 1
        return res
