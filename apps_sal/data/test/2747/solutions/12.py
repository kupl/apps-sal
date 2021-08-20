class Solution:

    def getRange(self, nums, index):
        prev = index
        after = index
        while prev >= 0 and nums[prev] == nums[index]:
            prev -= 1
        while after < len(nums) and nums[after] == nums[index]:
            after += 1
        return [prev + 1, after - 1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        m = int(len(nums) / 2)
        if target == nums[0]:
            return self.getRange(nums, 0)
        elif target == nums[-1]:
            return self.getRange(nums, len(nums) - 1)
        elif target == nums[m]:
            return self.getRange(nums, m)
        elif target < nums[0] or target > nums[-1]:
            return [-1, -1]
        elif target < nums[m]:
            return self.searchRange(nums[:m], target)
        else:
            tempRange = self.searchRange(nums[m:], target)
            if tempRange[0] == -1:
                return [-1, -1]
            else:
                return [r + m for r in tempRange]
