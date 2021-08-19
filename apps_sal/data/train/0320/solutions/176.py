class Solution:

    def minOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        step = 0
        while any((n > 0 for n in nums)):
            if all((n % 2 == 0 for n in nums)):
                nums = [n // 2 for n in nums]
                step += 1
            else:
                remain_idx = []
                for (i, v) in enumerate(nums):
                    if v % 2 == 1:
                        nums[i] = nums[i] - 1
                        step += 1
        return step
