class Solution:
     def jump(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) <= 2:
             return len(nums)-1
         stack = []
         i = len(nums) - 2
         while i >= 0:
 #            print(nums,stack)
             if nums[i] == 1:
                 stack.append(i)
             elif nums[i] >= (len(nums)-1-i):
                 if stack:
                     stack.clear()    
                 stack.append(i)
             else:
                 j = 0
                 while stack and j < len(stack): 
                     if nums[i] >= (stack[j]-i):
                         stack = stack[0:j+1]
                         stack.append(i)
                         break
                     else:
                         j += 1
             i -= 1
 #        print(stack)
         return len(stack)
                     

