class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        count=0
        j=len(nums)-1
        while i<len(nums) and nums[i]*2<=target:
            #count+=1
            while i<j and nums[i]+nums[j]>target:
                j-=1
                
            #print(i,j,nums[i],nums[j])
            count+=2**(j-i)
            i+=1
        return count%(10**9+7)
