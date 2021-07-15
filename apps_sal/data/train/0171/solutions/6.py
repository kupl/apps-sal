class Solution:
     def maxProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         dp_max=[0]*len(nums)
         dp_min=[0]*len(nums)
         res=dp_max[0]=dp_min[0]=nums[0]
         
         for i in range(1,len(nums)):
             dp_max[i]=max(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i])
             dp_min[i]=min(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i])
             res=max(res,dp_max[i])
         return res
