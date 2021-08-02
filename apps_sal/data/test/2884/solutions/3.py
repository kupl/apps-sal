class Solution:
    def combinationSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(a, i, target):
            for j in range(i, len(nums)):
                if target <= nums[j]:
                    if target == nums[j]:
                        ans.append(a + [nums[j]])
                    break
                if i == j or nums[j] != nums[j - 1]:
                    dfs(a + [nums[j]], j + 1, target - nums[j])

        ans = []
        nums.sort()
        dfs([], 0, target)
        return ans
