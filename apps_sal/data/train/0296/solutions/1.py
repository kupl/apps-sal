class Solution:
     def findMin(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         #类似上一题
         if not nums:
             return -1
         l,r=0,len(nums)-1
         #二分
         while l<=r:
             mid=(l+r)//2
             # 后半递增
             if nums[mid]<nums[r]:
                 r=mid
             else:
                 #类似上一题
                 if nums[mid]>nums[r]:
                     l=mid+1
                 #这里处理重复数
                 else:
                     r-=1
         if nums[l]<nums[r]:
             return nums[l]
         else:
             return nums[r]
