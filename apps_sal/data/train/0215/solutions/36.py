class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        #         primeSet = set()
        #         def isPrime(x):
        #             if x < 2 or x in primeSet:
        #                 return False
        #             i = 2
        #             limit = int(x**0.5)
        #             while i < limit +1:
        #                 if x%i == 0:
        #                     return False
        #                 limit = x//i
        #                 i += 1
        #             primeSet.add(x)
        #             return True

        #         numsLen = len(nums)
        #         primeCounter = 0
        #         for i in range(numsLen):
        #             if nums[i] == 1:
        #                 return True
        #             if isPrime(nums[i]):
        #                 primeCounter += 1
        #                 if primeCounter == 2:
        #                     return True
        #             else:
        #                 for j in range(i):
        #                     if isPrime(abs(nums[j] - nums[i])):
        #                         primeCounter += 1
        #                         if primeCounter == 2:
        #                             return True
        #         return False
        g = nums[0]
        for i in nums:
            g = gcd(i, g)
        return g == 1
