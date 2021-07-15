class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while True:
            for i, x in enumerate(nums):
                if x % 2 != 0:
                    nums[i] -= 1
                    res += 1
            if sum(nums) == 0: break
            nums = [x // 2 for x in nums]
            res += 1
            if sum(nums) == 0: break

        return res
