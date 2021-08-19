class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        change = 0
        while sum(nums):
            change = 0
            for i in range(len(nums)):
                if nums[i] % 2:
                    ret += 1
                    nums[i] -= 1
                    change = 1
            if change == 0:
                ret += 1
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
        return ret
