class Solution:

    def minOperations(self, nums: List[int]) -> int:
        c = 0
        while True:
            c0 = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    c += 1
                    nums[i] = (nums[i] - 1) // 2
                else:
                    nums[i] = nums[i] // 2
                if nums[i] == 0:
                    c0 += 1
            if c0 == len(nums):
                return c
            else:
                c += 1
