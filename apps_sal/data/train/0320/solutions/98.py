class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        doubles = 0
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    ones += 1
            if sum(nums) != 0:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                doubles += 1
        return ones + doubles
