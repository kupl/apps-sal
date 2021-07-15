class Solution:
     def firstMissingPositive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         lnums=len(nums)
         for i in range(lnums):
             while 0<nums[i]<=lnums and nums[i]!=nums[nums[i]-1]:
                 tmp=nums[i]
                 print((i,tmp,nums))
                 nums[tmp-1],nums[i]=nums[i],nums[tmp-1]
                 print((i,tmp,nums))
         for i in range(lnums):
             if nums[i]!=i+1:
                 return i+1
         return lnums+1
         
         

