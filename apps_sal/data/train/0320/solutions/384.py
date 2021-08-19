class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            op = False
            zeroes = 0
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    count += 1
                    nums[i] -= 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    zeroes += 1
                else:
                    nums[i] = nums[i] // 2
                    op = True
            if op:
                count += 1
            if zeroes == len(nums):
                return count
