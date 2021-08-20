class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable_so_far = 0
        for i in range(len(nums)):
            if reachable_so_far < i:
                return False
            if reachable_so_far >= len(nums) - 1:
                return True
            reachable_so_far = max(reachable_so_far, i + nums[i])
