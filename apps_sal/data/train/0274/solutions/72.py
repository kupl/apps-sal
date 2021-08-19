class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        left = 0
        right = 0

        curr_min = nums[0]
        curr_max = nums[0]

        max_len = 1

        # while left <= right and right < len(nums):
        for right in range(len(nums)):
            curr_max = max(curr_max, nums[right])
            curr_min = min(curr_min, nums[right])

            if curr_max - curr_min <= limit:
                max_len = max(max_len, right - left + 1)

            else:
                if nums[left] == curr_max:

                    curr_max = max(nums[left + 1: right + 1])

                if nums[left] == curr_min:
                    curr_min = min(nums[left + 1: right + 1])
                left += 1
        return max_len
