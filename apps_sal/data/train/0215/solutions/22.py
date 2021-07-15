class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for num in nums:
            while num:
                gcd, num = num, gcd % num
            if gcd == 1:
                return True
        return False

