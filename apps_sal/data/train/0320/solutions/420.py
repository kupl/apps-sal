class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        s = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] -= 1
                s += 1
        if s == 0:
            for i in range(len(nums)):
                nums[i] //= 2
            s += 1
        return self.minOperations(nums) + s
