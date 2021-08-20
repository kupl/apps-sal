class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        ans = 1
        minNum = nums[0]
        maxNum = nums[0]
        i = 0
        j = 0
        n = len(nums)
        while i < n and j < n:
            maxNum = max(maxNum, nums[i])
            minNum = min(minNum, nums[i])
            if abs(maxNum - minNum) > limit:
                if nums[j] == maxNum:
                    maxNum = max(nums[j + 1:i + 1])
                elif nums[j] == minNum:
                    minNum = min(nums[j + 1:i + 1])
                j += 1
            else:
                ans = max(ans, i - j + 1)
            i += 1
        return ans
