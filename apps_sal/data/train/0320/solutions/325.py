class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        total = sum(nums)

        while total != 0:
            evens = 0
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    res += 1
                    total -= 1
                else:
                    evens += 1

            if evens == len(nums):
                for i in range(len(nums)):
                    nums[i] /= 2
                    total -= nums[i]
                res += 1

        return res
