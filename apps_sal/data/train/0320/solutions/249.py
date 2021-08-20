class Solution:

    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while True:
            doDivision = 0
            NoZero = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    NoZero = 0
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    op += 1
                if nums[i] != 1 and nums[i] != 0:
                    doDivision = 1
                    nums[i] //= 2
            if doDivision == 1:
                op += 1
            if NoZero == 1:
                return op
