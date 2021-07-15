class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x,y):
            while y:
                x,y=y,x%y
            return x
        g=nums[0]
        for x in nums:
            g=gcd(g,x)
        return g==1

