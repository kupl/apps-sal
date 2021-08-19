class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:

        def gcd(x, y):
            if y > x:
                return gcd(y, x)
            if y == 0:
                return x
            return gcd(y, x % y)
        cur = nums[0]
        for i in range(1, len(nums)):
            cur = gcd(cur, nums[i])
        return cur == 1
