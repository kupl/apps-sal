class Solution:
     def deleteAndEarn(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return 0
         
         nums.sort()
         a = [0]*len(nums)
         b = [0]*len(nums)
         k = -1
         a[-1] = nums[-1]
         b[-1] = 0
         for i in range(len(nums)-2, -1, -1):
             print(nums[i], nums[i+1])
             if nums[i] == nums[i+1]-1:
                 a[i] = max(a[k], b[k])+nums[i] if k!=-1 else nums[i]
                 b[i] = max(a[i+1], b[i+1])
             elif nums[i] == nums[i+1]:
                 a[i] = a[i+1]+nums[i]
                 b[i] = b[i+1]
             else:
                 a[i] = max(a[i+1], b[i+1])+nums[i]
                 b[i] = max(a[i+1], b[i+1])
             if nums[i] < nums[i+1]:
                 k = i+1
 
         return(max(a[0], b[0]))
