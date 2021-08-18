class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        left = 0
        right = 1
        cur_max = cur_min = nums[0]
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
