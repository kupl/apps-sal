class Solution:
     def lengthOfLongestSubstring(self, s):
         """
         :type s: str
         :rtype: int
         """
         head = 0
         dic = {}
         res = 0
         for i in range(len(s)):
             if s[i] in dic and dic[s[i]] >= head:
                 res = max(res, i-head)
                 head = dic[s[i]]+1
             dic[s[i]] = i
         return max(res, len(s)-head)

