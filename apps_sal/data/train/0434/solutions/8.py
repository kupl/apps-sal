class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        left = 0
        x = 1
        for right in range(len(nums)):
            if not nums[right]:
                x -= 1
            while x < 0:
                if not nums[left]:
                    x += 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest - 1
