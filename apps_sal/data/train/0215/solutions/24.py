class Solution:
    def gcd(self, nums):
        g = nums[0]
        for x in nums:
            while x:
                g, x = x, g % x
        return g

    def bezout(self, a: [int], d):
        if self.gcd(a) == d:
            return True
        return False

    def isGoodArray(self, nums: [int]) -> bool:
        return self.bezout(nums, 1)
