class Solution:
    def minOperations(self, nums: List[int]) -> int:

        Count = 0

        while True:

            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    Count += 1
                    nums[i] = (nums[i] - 1) // 2
                else:
                    nums[i] = nums[i] // 2

            if sum(nums) == 0:
                return Count
            Count += 1
