class Solution:
     def wiggleMaxLength(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         l = len(nums)
         if l == 0:
             return 0
         elif l == 1:
             return 1
         st = 1
         while nums[0] == nums[st]:
             st += 1
             if st == l:
                 return 1
         one, two = (nums[0], nums[st])
         cnt = 2
         for i in range(st+1, l):
             if nums[i] == two:
                 continue
             if one < two:
                 if nums[i] > two:
                     two = nums[i]
                 else:
                     one = two
                     two = nums[i]
                     cnt += 1
             else:
                 if nums[i] < two:
                     two = nums[i]
                 else:
                     one = two
                     two = nums[i]
                     cnt += 1
         return cnt
