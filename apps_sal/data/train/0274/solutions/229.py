class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1
        left = right = 0
        min_n = max_n = nums[0]
        max_size = 0
        while right < len(nums):
            if nums[right] > max_n:
                max_n = nums[right]
            if nums[right] < min_n:
                min_n = nums[right]
            while max_n - min_n > limit:
                left += 1
                min_n = min(nums[left:right + 1])
                max_n = max(nums[left:right + 1])
                break
            if right - left > max_size:
                max_size = right - left
            right += 1
        return max_size + 1
