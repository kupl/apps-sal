class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        low, high = 0, 0
        cn = 0
        ans = 0

        while low < len(nums) and high < len(nums):
            if nums[high] == 0:
                if cn < 1:
                    cn += 1
                else:
                    while nums[low] != 0:
                        low += 1
                    low += 1
            high += 1
            ans = max(ans, high - low)

        return max(ans, high - low) - 1
