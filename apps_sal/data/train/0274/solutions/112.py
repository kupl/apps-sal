class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen = 1
        curMax = curMin = nums[0]
        l = r = 0
        while r < len(nums):
            curMax = max(curMax, nums[r])
            curMin = min(curMin, nums[r])
            if curMax - curMin <= limit:
                maxLen = max(maxLen, r - l + 1)
            else:
                if nums[l] == curMin:
                    curMin = min(nums[l + 1:r + 1])
                if nums[l] == curMax:
                    curMax = max(nums[l + 1:r + 1])
                l += 1
            r += 1
        return maxLen
