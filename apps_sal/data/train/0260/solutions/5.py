class Solution:
     def wiggleMaxLength(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return 0
         if len(nums) == 1:
             return 1
         N = len(nums)
         sol = [0 for _ in nums]
         sol[0] = [1,1] #starting with -, starting with +
         for i in range(1,N):
             new = [0,0]
             if nums[i] > nums[i-1]:
                 new[0] = sol[i-1][1]+1
             else:
                 new[0] = sol[i-1][0]
             if nums[i] < nums[i-1]:
                 new[1] = sol[i-1][0]+1
             else:
                 new[1] = sol[i-1][1]
             sol[i] = new
         return max(sol[-1])
             
                 

