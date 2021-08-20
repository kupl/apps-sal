class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i in range(len(nums)):
            if i > m:
                return False
            m = max(m, nums[i] + i)
        return True
