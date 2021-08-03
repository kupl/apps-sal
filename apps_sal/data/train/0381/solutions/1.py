class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = float('inf')
        left = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                result = min(result, i + 1 - left)
                total -= nums[left]
                left += 1
        return 0 if result == float('inf') else result
