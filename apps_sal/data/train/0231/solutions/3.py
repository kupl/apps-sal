class Solution:
     def firstMissingPositive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         i = 0
         n = len(nums)
         
         if not nums:
             return(1)
         while (i <n):
             while ((nums[i] != i) and (nums[i] > 0) and (i<n) and (nums[i] < n) and (nums[i] != nums[nums[i]])):
                 temp = nums[nums[i]]
                 nums[nums[i]] = nums[i]
                 nums[i] = temp
             i = i + 1
 
         i = 1
         while(i<n):
             if(nums[i] != i):
                 return(i)
             i=i+1
         if(nums[0] == n):
             return(n+1)
         else:
             return(n)
 

