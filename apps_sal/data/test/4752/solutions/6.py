class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = dict()
        l = len(nums)
        if l <= 1:
            return []
        for i in range(l):
            t[nums[i]] = i
        for i in range(l):
            comp = target - nums[i]
            if comp in t and t[comp] != i:
                return [i, t[comp]]
        return []
