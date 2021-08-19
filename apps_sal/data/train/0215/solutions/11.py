class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:

        def gcd(a, b):
            (a, b) = (max(a, b), min(a, b))
            while b:
                (a, b) = (b, a % b)
            return a
        if len(nums) == 1:
            if nums != [1]:
                return False
            else:
                return True
        i = 0
        d = nums[0]
        while i < len(nums):
            d = gcd(nums[i], d)
            if d == 1:
                return True
            i += 1
        return False
