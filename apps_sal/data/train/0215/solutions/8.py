class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return nums[0] == 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_val = nums[0]
        for i in range(1, len(nums)):
            gcd_val = gcd(gcd_val, nums[i])
            if gcd_val == 1:
                return True
        return False
