class Solution:

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(depth, start, cur):
            if cur not in res:
                res.append(cur)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, cur + [nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return list(res)
