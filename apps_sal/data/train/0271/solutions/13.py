class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        near = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if near <= i + nums[i]:
                near = i

        return near == 0
