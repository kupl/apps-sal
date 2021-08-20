class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        cur_max = nums[0]
        cur_min = nums[0]
        l = 0
        r = 1
        max_l = 1
        while l <= r and r < len(nums):
            cur_max = max(cur_max, nums[r])
            cur_min = min(cur_min, nums[r])
            if cur_max - cur_min <= limit:
                max_l = max(max_l, r - l + 1)
            else:
                if nums[l] == cur_max:
                    cur_max = max(nums[l + 1:r + 1])
                if nums[l] == cur_min:
                    cur_min = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return max_l
