class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        # left and right index to take out the substring
        left = 0
        right = 1
        # let current max and min equal to the first number
        cur_max = cur_min = nums[0]
        # the max lense of the target substring is at least 1
        max_len = 1

        while right < len(nums):
            cur_max = max(cur_max, nums[right])
            cur_min = min(cur_min, nums[right])

            if cur_max - cur_min <= limit:
                max_len = max(max_len, right - left + 1)
            else:
                if nums[left] == cur_max:
                    cur_max = max(nums[left + 1:right + 1])
                if nums[left] == cur_min:
                    cur_min = min(nums[left + 1:right + 1])
                left += 1
            right += 1
        return max_len
