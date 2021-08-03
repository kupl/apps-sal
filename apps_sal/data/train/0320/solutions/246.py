class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zeros, ops = 0, 0
        while zeros != len(nums):
            odds, evens, zeros = 0, 0, 0
            for i in range(0, len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    odds += 1

                if nums[i] == 0:
                    zeros += 1
                else:
                    evens += 1
                    nums[i] //= 2
            ops += odds
            ops += 1 if evens else 0
        return ops
