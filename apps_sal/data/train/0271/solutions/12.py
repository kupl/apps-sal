class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums) - 1
        i = last
        while i >= 0:
            if nums[i] + i >= last:
                last = i
            i -= 1
        return last == 0
