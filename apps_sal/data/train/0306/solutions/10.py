class Solution:

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.use_dp(nums, target)

    def use_dfs(self, nums, target):
        self.result = 0
        nums.sort()
        self.dfs(nums, target)
        return self.result

    def dfs(self, nums, target):
        if target == 0:
            self.result += 1
            return
        for num in nums:
            if num > target:
                break
            self.dfs(nums, target - num)

    def use_recursion_dp(self, nums, target):
        dp = [-1] * (target + 1)
        dp[0] = 1
        nums.sort()
        return self.dp_dfs(nums, target, dp)

    def dp_dfs(self, nums, target, dp):
        if dp[target] != -1:
            return dp[target]
        result = 0
        for num in nums:
            if num > target:
                break
            result += self.dp_dfs(nums, target - num, dp)
        dp[target] = result
        return result

    def use_dp(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for item in range(1, len(dp)):
            for num in nums:
                if item - num >= 0:
                    dp[item] += dp[item - num]
        return dp[target]
