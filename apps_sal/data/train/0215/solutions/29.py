class Solution:

    def gcd(x, y):
        gcd_ = i
        for i in range(2, min(x, y)):
            if x % i == 0 and y % i == 0:
                gcd_ = i
        return gcd_

    def isGoodArray(self, nums: List[int]) -> bool:
        start = nums[0]
        for i in nums:
            start = gcd(start, i)
        return start == 1
