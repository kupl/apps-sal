class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    res += 1
                    nums[i] -= 1
            if sum(nums) != 0:
                res += 1
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
        return res
