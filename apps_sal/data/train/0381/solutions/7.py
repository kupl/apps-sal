class Solution:

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        ans = len(nums)
        left = 0
        temps = 0
        for i in range(len(nums)):
            temps += nums[i]
            while temps >= s:
                ans = min(ans, i + 1 - left)
                temps -= nums[left]
                left += 1
        return ans
