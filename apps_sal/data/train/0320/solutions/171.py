import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #         res = 0
        #         maxPow = 0
        #         for i in range(len(nums)):
        #             if nums[i] > 0:
        #                 power = round(math.log(nums[i])/math.log(2))
        #                 print(power, pow(2, power))
        #                 if maxPow < power:
        #                     maxPow = power
        #                 res += 1 + nums[i] - pow(2, power)

        #         res += maxPow
        #         return res
        res = 0
        while True:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    res += 1
                    nums[i] -= 1

            numZeros = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    numZeros += 1

            if numZeros == len(nums):
                break

            for i in range(len(nums)):
                nums[i] //= 2
            res += 1

        return res
