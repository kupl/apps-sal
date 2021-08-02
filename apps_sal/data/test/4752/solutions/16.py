class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes = dict([(nums[i], i) for i in range(len(nums))])
        for i in range(len(nums)):
            if target - nums[i] in indexes and indexes[target - nums[i]] != i:
                return [i, indexes[target - nums[i]]]
        return []
