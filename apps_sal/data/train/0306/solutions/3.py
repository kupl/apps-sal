class Solution:
    # recursive, time limit exceeded
    def combinationSum4_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        if target == 0:
            return 1

        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum4(nums, target - nums[i])
        return res

    # top down using memory
    def combinationSum4_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1] * (target + 1)
        dp[0] = 1
        return self.helper(dp, nums, target)

    def helper(self, dp, nums, target):
        if dp[target] != -1:
            return dp[target]

        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.helper(dp, nums, target - nums[i])
        dp[target] = res
        return res

    # bottom up
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in sorted(nums):
                if i < num:
                    break
                dp[i] += dp[i - num]
        return dp[-1]
