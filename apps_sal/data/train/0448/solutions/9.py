class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         if not k:
             i=0
             while i<len(nums)-1:
                 if not nums[i] and not nums[i+1]:
                     return True
                 i+=1
             return False
         k=abs(k)
 
         dic={0:-1}
         rem=0   # remainder
         i=0
         while i< len(nums):
             rem=(rem+nums[i])%k
             if rem not in dic: dic[rem]=i
             elif dic[rem]<i-1: return True
             i+=1
         return False
 

