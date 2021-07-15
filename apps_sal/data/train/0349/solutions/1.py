class Solution:
     def deleteAndEarn(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if (nums == []):
             return 0
         if (len(nums) == 1):
             return nums[0]
         
         nums.sort()
         numsp = nums[0]
         choose = [0,nums[0]]
         for i in range(1,len(nums)):
           numsc = nums[i]
           if (numsc == numsp):
               choose[1] += numsc
               continue
           elif(numsc == numsp+1):
               temp = choose[0]
               choose[0] = max(choose)
               choose[1] = temp+numsc
               numsp = numsc
           else:
               choose[0] = max(choose)
               choose[1] = choose[0]+numsc
               numsp = numsc
               
         return max(choose)
