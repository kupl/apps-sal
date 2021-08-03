class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res, [False] * len(nums))
        return res

    def dfs(self, nums, path, res, used):
        if len(path) == len(nums):
            res.append(path)
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                self.dfs(nums, path + [nums[i]], res, used)
                used[i] = False
