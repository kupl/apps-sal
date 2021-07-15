class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0]*2>target:
            return 0
        
        res=0
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                res+=2**(r-l)
                l+=1
            else:
                r-=1
        return res%(10**9+7)
