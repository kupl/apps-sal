class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        x = len(nums)
        for i in range(x):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap.get(comp), i]
            hashmap[nums[i]] = i
