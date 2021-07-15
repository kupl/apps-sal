class Solution:
     def minMoves2(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         med=0
         nums.sort()
         final=0
         final1=0
         if len(nums)%2!=0:
             med=int(len(nums)/2)
             for j in range(med):
                 final=final+abs(nums[med]-nums[j])
             for g in range(med,len(nums)):
                 final=final+abs(nums[med]-nums[g])
                 
         else:
             med=int(len(nums)/2)
             for k in range(med):
                 final=final+abs(nums[med]-nums[k])
             for t in range(med,len(nums)):
                 final=final+abs(nums[med]-nums[t])
             
             med=int(len(nums)/2)-1
             for h in range(med):
                 final1=final1+abs(nums[med]-nums[h])
             for q in range(med,len(nums)):
                 final1=final1+abs(nums[med]-nums[q])
             final=min(final,final1)
         return final
