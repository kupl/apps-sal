class Solution:

    def subsets(self, nums):
        if len(nums) == 0:
            return [[]]
        ret = []
        for (i, n) in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            for s in self.subsets(nums[i + 1:]):
                ret.append([n] + s)
        return [[]] + ret

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.subsets(nums)
