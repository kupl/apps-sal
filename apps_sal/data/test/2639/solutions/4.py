class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(nums, start, tmp, res):
            res.append(tmp[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    tmp.append(nums[i])
                    backtrack(nums, i + 1, tmp, res)
                    del tmp[-1]

        res = list()
        backtrack(sorted(nums), 0, [], res)
        return res
