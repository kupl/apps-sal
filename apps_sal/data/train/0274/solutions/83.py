class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        l = 0
        r = 1

        curr_max = nums[0]
        curr_min = nums[0]
        max_len = 1
        while l <= r and r < len(nums):

            curr_max = max(curr_max, nums[r])
            curr_min = min(curr_min, nums[r])

            if curr_max - curr_min <= limit:
                max_len = max(max_len, r - l + 1)

            else:

                if curr_max == nums[l]:
                    curr_max = max(nums[l + 1:r + 1])
                if curr_min == nums[l]:
                    curr_min = min(nums[l + 1:r + 1])
                l += 1

            r += 1

        return max_len
