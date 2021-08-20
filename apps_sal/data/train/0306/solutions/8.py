class Solution:

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(nums, target, memo):
            if target in memo:
                return memo[target]
            if target < 0:
                return
            if target == 0:
                memo[target] = 1
                return
            memo[target] = 0
            for num in nums:
                dfs(nums, target - num, memo)
                if target - num >= 0:
                    memo[target] += memo[target - num]
        dfs.count = 0
        nums.sort()
        memo = {}
        dfs(nums, target, memo)
        return memo[target]
