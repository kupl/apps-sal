class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for n in nums:
            while n:
                gcd, n = n, gcd % n

        return gcd == 1
