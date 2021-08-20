class Solution:

    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while True:
            doDivision = 0
            AllZero = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    AllZero = 0
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    op += 1
                if nums[i] != 1 and nums[i] != 0:
                    doDivision = 1
                    nums[i] //= 2
            if doDivision == 1:
                op += 1
            if AllZero == 1:
                return op
