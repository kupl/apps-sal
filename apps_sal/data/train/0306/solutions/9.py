class Solution:

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.dp = [-1] * (target + 1)
        self.dp[0] = 1
        return self.cSUtil(nums, target)

    def cSUtil(self, nums, target):
        if target < 0:
            return 0
        if self.dp[target] != -1:
            return self.dp[target]
        res = 0
        for num in nums:
            target -= num
            res += self.cSUtil(nums, target)
            target += num
        self.dp[target] = res
        return res
