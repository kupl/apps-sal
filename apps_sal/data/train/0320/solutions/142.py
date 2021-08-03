class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        check = 0
        if not nums:
            return(0)
        while check != len(nums):
            x, check, nums = self.odd(nums)
            count += x
            if check == len(nums):
                return(count)
            nums = self.div(nums)
            count += 1

    def div(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] // 2
        return(nums)

    def odd(self, nums):
        a = 0
        b = 0

        for i in range(len(nums)):
            if nums[i] & 1 == 1:
                a += 1
                nums[i] -= 1
            if nums[i] == 0:
                b += 1
        return(a, b, nums)
