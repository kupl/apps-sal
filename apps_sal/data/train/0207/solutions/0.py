class Solution:
     def largestNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: str
         """
         nums = [str(n) for n in nums]
         
         nums.sort(reverse=True)
         
         for i in range(1, len(nums)):
             if len(nums[i-1]) > len(nums[i]):
                 ran = len(nums[i])
                 j = i
                 while j-1 >= 0 and nums[j-1][:ran] == nums[j] and nums[j-1]+nums[j]<=nums[j]+nums[j-1]:
                     nums[j-1], nums[j] = nums[j], nums[j-1]
                     j -= 1
                     
         return str(int(''.join(nums)))
