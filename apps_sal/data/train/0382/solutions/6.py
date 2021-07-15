class Solution:
     def findPeakElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
 #         left = 0
 #         right = len(nums)-1
 
   
 #         while left < right-1:
 #             mid = (left+right)//2
 #             if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
 #                 return mid
 
 #             if nums[mid] < nums[mid+1]:
 #                 left = mid+1
 #             else:
 #                 right = mid-1
 
       
 #         return left if nums[left] >= nums[right] else right
         n = len(nums)
         if n == 0:
             return null
         if n == 1:
             return 0
         if nums[0] > nums[1]:
             return 0
         
         for ind in range(1,len(nums)-1):
             print(ind)
         
             if nums[ind] > nums[ind-1] and nums[ind] > nums[ind+1]:
                 return ind
         
         if nums[n-1] > nums[n-2]:
             print('haha')
             return n-1
         

