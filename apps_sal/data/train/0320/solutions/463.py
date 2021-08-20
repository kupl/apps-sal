class Solution:

    def odds(self, nums):
        ops = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] -= 1
                ops += 1
        return (nums, ops)

    def opsc(self, nums, final):
        if nums == final:
            return 0
        (nums, ops) = self.odds(nums)
        if nums == final:
            return ops
        for i in range(len(nums)):
            nums[i] /= 2
        ops += 1
        ops += self.opsc(nums, final)
        return ops

    def minOperations(self, nums: List[int]) -> int:
        final = []
        for i in range(len(nums)):
            final.append(0)
        return self.opsc(nums, final)
