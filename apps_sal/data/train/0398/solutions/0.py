class Solution:
     def subarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         
         dic = {}
         numSum = 0
         dic[0] = 1
         ans = 0
         for i in range(len(nums)):
             numSum += nums[i]
             if (numSum - k) in dic:
                 ans += dic[numSum - k]
             if numSum in dic:
                 dic[numSum] += 1
             else:
                 dic[numSum] = 1
         return ans
