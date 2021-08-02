class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        for i, num in enumerate(nums):
            if target - num in numsMap:
                return [i, numsMap[target - num]]
            numsMap[num] = i
        return [None, None]
