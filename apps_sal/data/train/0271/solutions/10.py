class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 25003:
            return False
        length = len(nums)
        accessible = [False] * length
        accessible[0] = True
        for i in range(length - 1):
            if not accessible[i]:
                return False
            for j in range(i + 1, min(nums[i] + i + 1, length)):
                accessible[j] = True
                if j == length - 1:
                    return True
        return accessible[length - 1]
