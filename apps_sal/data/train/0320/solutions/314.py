class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while nums != [0] * len(nums):
            for i in range(len(nums)):
                if nums[i] == 1:
                    nums[i] -= 1
                    res += 1
                elif nums[i] % 2 == 1:
                    nums[i] -= 1
                    res += 1
            if nums == [0] * len(nums):
                break
            for i in range(len(nums)):
                nums[i] //= 2
            res += 1
        return res
