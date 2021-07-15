class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right=len(nums)-1
        res=0
        for i in range(len(nums)):
            while nums[i]+nums[right]>target and i<=right:
                right-=1
            if i<=right:
                res+=2**(right-i)
                res=res%((10**9)+7) 
        return res

