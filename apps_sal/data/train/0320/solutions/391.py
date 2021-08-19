class Solution:

    def minOperations(self, nums: List[int]) -> int:
        zeros = [0 for el in nums]
        res = 0
        while nums != zeros:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    res += 1
            if nums == zeros:
                break
            nums = [el / 2 for el in nums]
            res += 1
        return res
