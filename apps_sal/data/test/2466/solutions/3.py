class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        if not nums or len(nums) == 0:
            return self.res
        self.dfs(0, [], nums)
        return self.res

    def dfs(self, i, path, remaining):
        if len(remaining) == 0:
            self.res.append(path)
        for i in range(len(remaining)):
            self.dfs(i + 1, path + [remaining[i]], remaining[0:i] + remaining[i + 1:])
