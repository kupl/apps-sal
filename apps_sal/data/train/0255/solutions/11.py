class Solution:
     def jump(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return 0
         dic = {}
         length = len(nums)
         dic[length - 1] = 0
         for j in range(length - 1)[::-1]:
             #print(length - j + 1)
             if(nums[j] >= nums[j + 1] + 1 and not j + 1 == length - 1):
                 minstep = dic[j + 1] - 1
                 for k in range(max(3, nums[j+1] + 2) ,min(length - j , nums[j] + 1)):
                     #print(j,k)
                     if dic[j + k] < minstep:
                         minstep = dic[j + k]
                 dic[j] = minstep + 1
                 continue
             minstep = dic[j + 1]
             for k in range(2,min(length - j , nums[j] + 1)):
                 #print(j,k)
                 if dic[j + k] < minstep:
                     minstep = dic[j + k]
             dic[j] = minstep + 1
         #print(dic)
         return dic[0]
