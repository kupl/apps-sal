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
         seq = [nums[0], nums[st]]
         for i in range(st+1, l):
             if nums[i] == seq[-1]:
                 continue
             if seq[-1] < seq[-2]:
                 if nums[i] < seq[-1]:
                     seq[-1] = nums[i]
                 else:
                     seq.append(nums[i])
             else:
                 if nums[i]>seq[-1]:
                     seq[-1] = nums[i]
                 else:
                     seq.append(nums[i])
         return len(seq)
