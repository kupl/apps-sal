class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        l = 0
        r = 1
        curmax = nums[0]
        curmin = nums[0]
        maxlen = 1
        while l <= r and r < len(nums):
            curmax = max(curmax, nums[r])
            curmin = min(curmin, nums[r])
            if curmax - curmin <= limit:
                maxlen = max(maxlen, r - l + 1)
            else:
                if nums[l] == curmax:
                    curmax = max(nums[l + 1:r + 1])
                if nums[l] == curmin:
                    curmin = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return maxlen
