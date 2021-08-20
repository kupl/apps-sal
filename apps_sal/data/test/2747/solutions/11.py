class Solution:

    def getRange(self, nums, index):
        prev = index - 1
        after = index + 1
        while prev >= 0 and nums[prev] == nums[index]:
            prev -= 1
        while after < len(nums) and nums[after] == nums[index]:
            after += 1
        return [prev + 1, after - 1]

    def getIndex(self, nums, target):
        if nums == [] or target < nums[0] or target > nums[-1]:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        m = int(len(nums) / 2)
        if target < nums[m]:
            return self.getIndex(nums[:m], target)
        else:
            return -1 if self.getIndex(nums[m:], target) < 0 else self.getIndex(nums[m:], target) + m

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = self.getIndex(nums, target)
        if index == -1:
            return [-1, -1]
        else:
            return self.getRange(nums, index)
