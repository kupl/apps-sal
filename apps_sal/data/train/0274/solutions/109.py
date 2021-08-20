class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        l = 0
        r = 1
        cur_mx = nums[0]
        cur_mn = nums[0]
        max_l = 1
        while l <= r and r < len(nums):
            cur_mx = max(cur_mx, nums[r])
            cur_mn = min(cur_mn, nums[r])
            if cur_mx - cur_mn <= limit:
                max_l = max(max_l, r - l + 1)
            else:
                if nums[l] == cur_mx:
                    cur_mx = max(nums[l + 1:r + 1])
                if nums[l] == cur_mn:
                    cur_mn = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return max_l
