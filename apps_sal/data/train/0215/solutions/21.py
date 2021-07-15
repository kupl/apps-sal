class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g=nums[0]
        for i in nums:g=gcd(i,g)
        return g==1
