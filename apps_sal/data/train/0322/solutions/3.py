class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        missed, added, i = 1, 0, 0
        while missed <= n:
            if i < len(nums) and nums[i] <= missed:
                missed += nums[i]
                i += 1
            else:
                missed += missed
                added += 1
        return added
