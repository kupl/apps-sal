class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        if self.check(nums):
            return cnt
        while not self.check(nums):
            for i in range(len(nums)):
                cnt += nums[i] % 2
            cnt += 1
            self.divide2(nums)
        return cnt - 1

    def check(self, nums):
        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        return True

    def divide2(self, nums):
        for i in range(len(nums)):
            nums[i] //= 2
