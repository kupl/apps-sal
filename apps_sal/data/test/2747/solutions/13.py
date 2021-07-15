class Solution:
     def searchRange(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
         start = 0
         end = len(nums) - 1
         mid = 0
         ans = [-1, -1]
         while (start <= end):
             mid = int((start + end) / 2)
             if (nums[mid] == target):
                 ans[0] = mid  
                 ans[1] = mid  
                   
                 i = mid - 1  
                 while i >= 0 and nums[i] == target:  
                     ans[0] = i  
                     i -= 1  
                   
                 i = mid + 1  
                 while i < len(nums) and nums[i] == target:  
                     ans[1] = i  
                     i += 1  
                       
                 break  
             elif (nums[mid] > target):
                 end = mid - 1
             else:
                 start = mid + 1
             
         return ans
         

