class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 1
        ans = 1
        currMax = nums[0]
        currMin = nums[0]

        while left <= right and right < len(nums):
            currMax = max(currMax, nums[right])
            currMin = min(currMin, nums[right])

            if currMax - currMin <= limit:
                ans = max(ans, right - left + 1)
            else:
                if nums[left] == currMax:
                    currMax = max(nums[left + 1: right + 1])
                if nums[left] == currMin:
                    currMin = min(nums[left + 1: right + 1])
                left += 1
            right += 1

        return ans
