class Solution:
    def gcd(self, nums):
        g = nums[0]
        for x in nums:
            while x:
                g, x = x, g % x
        return g

    # a: list of integers
    # d: desired GCD of the integers in a
    def bezout(self, a: [int], d):
        if self.gcd(a) == d:
            return True
        return False

    def isGoodArray(self, nums: [int]) -> bool:
        return self.bezout(nums, 1)
