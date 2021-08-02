class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums):
            if not nums:
                return [[]]
            dic = set()
            new = []
            for i in range(len(nums)):
                if nums[i] not in dic:
                    dic.add(nums[i])
                    new += [[nums[i]] + item for item in dfs(nums[: i] + nums[i + 1:])]
            return new

        return dfs(nums)
