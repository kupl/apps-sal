class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: List[int]
         """
         length=len(nums)
         ans=[]
         for i in set(nums):
             if nums.count(i)>length/3:
                 ans.append(i)
         return ans
