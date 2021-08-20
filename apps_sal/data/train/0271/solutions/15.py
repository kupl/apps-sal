class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return True
        status = [False] * (len(nums) - 1) + [True]
        curr = len(nums) - 1
        for j in range(len(nums) - 2, -1, -1):
            if status[min(len(nums) - 1, j + nums[j])]:
                for i in range(j, curr):
                    status[i] = True
                curr = j
        return status[0]
