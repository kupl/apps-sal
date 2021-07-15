class Solution:
     def twoSum(self, nums, target):
         
         """
         dic={}
         for i,now in enumerate(nums):
             dev = target - now
             if dev in dic:
                 return [dic[dev],i]
             dic[now]=i
         return None
         """
     
         
     #   old
         a=sorted(nums)
         
         for j in range(len(nums)):
             for k in range(j+1,len(nums)):
                 s = a[j]+a[k]
                 if s == target:
                     if a[j]==a[k]:
                         return [i for i,x in enumerate(nums) if x == a[k]]
                     else:
                         b=nums.index(a[j])
                         c=nums.index(a[k])
                         return [b,c]
                         
                 elif s>target:
                     break
                
         
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """

