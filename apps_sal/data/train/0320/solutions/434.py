class Solution:

    def minOperations(self, nums: List[int]) -> int:
        total = 0
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
        while zeros < len(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    if nums[i] == 0:
                        zeros += 1
                    total += 1
            allEven = True
            while allEven and zeros < len(nums):
                for i in range(len(nums)):
                    nums[i] = nums[i] >> 1
                    if nums[i] % 2 == 1:
                        allEven = False
                total += 1
        return total
