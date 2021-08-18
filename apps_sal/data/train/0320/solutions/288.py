class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_op = 0
        l = len(nums)
        target = l * [0]
        while nums != target:
            if all(i % 2 == 0 for i in nums):
                nums = [i / 2 for i in nums]
                n_op += 1
            else:
                for i in range(l):
                    if nums[i] % 2 == 1:
                        nums[i] -= 1
                        n_op += 1
        return n_op
