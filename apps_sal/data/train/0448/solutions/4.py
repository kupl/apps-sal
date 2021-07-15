class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         if k==0:
             i=1
             while i<len(nums):
                 if nums[i-1]==0 and nums[i]==0:
                     return True
                 i+=1
             return False    
         d=dict()
         d[0]=-1
         s=0
         for i,x in enumerate(nums):
             s+=x
             s=s%k
             if s in d :
                 if i-d[s]>1:
                     return True
             else:    
                 d[s]=i
         return False    

