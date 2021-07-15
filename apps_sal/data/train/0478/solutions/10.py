class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         '''
         dic = {}
         for num in nums:
             if num in dic and dic[num] == 2:
                 del dic[num]
             else:
                 dic[num] = dic.get(num, 0) + 1
         return [k for k in dic.keys()][0]
         '''
         #return (sum(set(nums))*3-sum(nums))//2
         one, two = 0, 0
         for num in nums:
             one, two = (~two&one&~num)|(~two&~one&num), (two&~one&~num)|(~two&one&num)
         return one

