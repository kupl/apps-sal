class Solution:
     def lengthOfLongestSubstring(self, s):
         """
         :type s: str
         :rtype: int
         """
         L, res, last = -1, 0, {}
         for R, char in enumerate(s):
             if char in last and last[char] > L:
                 L = last[char]
             elif R-L > res:
                 res = R-L
             last[char] = R
         return res
