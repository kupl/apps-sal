class Solution:
    def gcd(self,a,b):
        return a if b==0 else self.gcd(b,a%b)
    def isGoodArray(self, nums: List[int]) -> bool:
        nums=list(set(nums))
        n=len(nums)
        if n==1 and nums[0]==1:return True
        cur=nums[0]        
        for i in range(1,n):
            cur=self.gcd(cur,nums[i])
            if cur==1:return True
        return False
