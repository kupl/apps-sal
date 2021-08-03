class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for i in nums:
            g = self.hcfnaive(i, g)
        return g == 1

    def hcfnaive(self, a, b):
        if(b == 0):
            return a
        else:
            return self.hcfnaive(b, a % b)
