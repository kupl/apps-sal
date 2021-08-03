class Solution:
    def minOperations(self, nums: List[int]) -> int:

        self.count = 0

        def sub(nums):
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    self.count += 1
            return nums

        def divide_all(nums):
            for k in range(len(nums)):
                if nums[k] == 0 or nums[k] % 2 == 0:
                    nums[k] //= 2
                else:
                    return []
            return nums

        def zeros(nums):
            c = 0
            for n in nums:
                if n == 0:
                    c += 1
            return c

        sub(nums)
        while zeros(nums) < len(nums):
            divide_all(nums)
            self.count += 1
            sub(nums)

        return self.count
