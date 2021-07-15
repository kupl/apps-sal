class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if not nums: return False
        a=nums[0]
        for i in range(1, len(nums)):
            a=gcd(a,nums[i])
        return a==1
