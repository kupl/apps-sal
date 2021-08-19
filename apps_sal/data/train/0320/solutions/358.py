class Solution:
    def minOperations(self, nums: List[int]) -> int:

        steps = 0
        nums = sorted(nums)
        j = -1
        while(j < len(nums) - 1):  # not every elements are 0
            s = j + 1  # calculate steps for next non_zero item
            while s < len(nums):
                if nums[s] == 0:
                    j += 1
                elif nums[s] == 1:
                    steps += 1
                    j += 1
                    nums[s] = 0
                elif nums[s] % 2 == 1:
                    steps += 1
                    nums[s] -= 1
                    nums[s] //= 2
                else:
                    nums[s] //= 2
                s += 1
            if j != len(nums) - 1:
                steps += 1

        return steps
