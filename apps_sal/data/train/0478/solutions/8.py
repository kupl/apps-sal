class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            return nums[0]
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 2]:
                return nums[i]
        return nums[-1]
