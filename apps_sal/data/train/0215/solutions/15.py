class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            if b>0:
                return gcd(b, a%b)
            return a
        if not nums:
            return False
        if len(nums)==1:
            return nums[0]==1
        num = nums[0]
        for i in range(1, len(nums)):
            ans = gcd(num, nums[i])
            if ans==1:
                return True
            num = ans
        return False

