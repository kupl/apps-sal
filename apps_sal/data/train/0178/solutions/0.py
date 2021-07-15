class Solution:
     def lengthOfLIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return 0
         res = [nums[0]]
         def binarySearch(l,target):
             left , right = 0 , len(l)-1
             while left < right:
                 mid = (left + right)//2
                 if l[mid] >= target:
                     right = mid
                 else:
                     left = mid + 1
             return left
         for i in range(1,len(nums)):
             if nums[i] > res[-1]:
                 res.append(nums[i])
             else:
                 res[binarySearch(res,nums[i])] = nums[i]
         return len(res)

