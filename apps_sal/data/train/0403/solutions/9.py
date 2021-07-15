class Solution:
     def increasingTriplet(self, nums):
         
         if len(nums) == 0:
             n = 1
         else:
             n = len(nums)
             
         index_of_A = 0
         index_of_B = n-1
         A_indices = [None] * n
         B_indices = [None] * n
     
         for i in range(2, n):
             if nums[i-1] <= nums[index_of_A]:
                 index_of_A = i-1
                 A_indices[i-1] = None
             else:
                 A_indices[i-1] = index_of_A
             if nums[n-i] >= nums[index_of_B]:
                 index_of_B = n-i
                 B_indices[n-i] = None
             else:
                 B_indices[n-i] = index_of_B
      
         for i in range(0, n):
             if A_indices[i] != None and B_indices[i] != None:
                 return True
             
         return False
             

