class Solution:

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        res = []
        self.df(nums, 0, result, res)
        return res

    def df(self, nums, idx, result, res):
        if idx > len(nums):
            return
        if result not in res:
            res.append(result)
        for i in range(idx, len(nums)):
            self.df(nums, i + 1, sorted(result + [nums[i]]), res)
