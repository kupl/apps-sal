class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        n = len(nums)
        l = 0
        r = 1
        maxVal = nums[0]
        minVal = nums[0]
        res = 1
        while l < r and r < n:
            maxVal = max(maxVal, nums[r])
            minVal = min(minVal, nums[r])
            if maxVal - minVal <= limit:
                res = max(res, r - l + 1)
            else:
                if nums[l] == maxVal:
                    maxVal = max(nums[l + 1:r + 1])
                if nums[l] == minVal:
                    minVal = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return res
        return res
