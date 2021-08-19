class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:

        def gcd(x, y):
            if x < y:
                (x, y) = (y, x)
            if not x % y:
                return y
            return gcd(x % y, y)
        if len(nums) == 1:
            if nums[0] == 1:
                return True
            return False
        while True:
            x = nums.pop(-1)
            y = nums.pop(-1)
            z = gcd(x, y)
            if not nums:
                return z == 1
            nums.append(z)
