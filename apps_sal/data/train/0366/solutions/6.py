class Solution:
     def longestSubstring(self, s, k):
         """
         :type s: str
         :type k: int
         :rtype: int
         """
         # str.count is much faster than collections.Counter under certain conditions
         # collections.Counter is intended to be a general tool
         # while str.count is much optimized C code to do just one thing 
         # (Counter in Py3 is written in C too)
         # see this SO question:
         # https://stackoverflow.com/questions/41594940/why-is-collections-counter-so-slow
         for c in set(s):
             if s.count(c) < k:
                 return max(self.longestSubstring(sub, k) for sub in s.split(c))
         return len(s)
