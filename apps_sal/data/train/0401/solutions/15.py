class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        memo = {}
        self.helper(0, nums, memo)
        return memo[0, 0]

    def helper(self, index, nums, memo):
        if index == len(nums):
            memo[index, 0] = 0
            memo[index, 1] = 0
            memo[index, 2] = 0
        else:
            self.helper(index + 1, nums, memo)
            for i in range(3):
                if i != 0 and memo[index + 1, i] == 0:
                    memo[index, (i + nums[index]) % 3] = max(0, memo[index + 1, (i + nums[index]) % 3])
                else:
                    new_mod = (nums[index] + memo[index + 1, i]) % 3
                    new_sum = max(nums[index] + memo[index + 1, i], memo[index + 1, new_mod])
                    memo[index, new_mod] = new_sum
            return
