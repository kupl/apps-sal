class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        div, mod = divmod(_sum, 2)
        if mod or max(nums) > div:
            return False
        nums.sort(reverse=True)
        target = [div] * 2
        return self.dfs(nums, 0, target)

    def dfs(self, nums, index, target):
        for i in range(2):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if target[i] == 0 or self.dfs(nums, index + 1, target):
                    return True
                target[i] += nums[index]
        return False
