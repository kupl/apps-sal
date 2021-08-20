class Solution:

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = [[]]
        self._helpFun(nums, res, [])
        return res

    def _helpFun(self, nums, res, curr):
        if not nums:
            if curr not in res:
                res.append(curr)
            return
        for i in range(len(nums)):
            newCurr = curr + [nums[i]]
            if newCurr not in res:
                res.append(newCurr)
            self._helpFun(nums[i + 1:], res, newCurr)
