class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            zeros = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    continue
                else:
                    nums[i] -= 1
                    count += 1
            for j in range(len(nums)):
                if nums[j] == 0:
                    zeros += 1
                nums[j] = nums[j] // 2
            if zeros == len(nums):
                return count
            count += 1
