class Solution:
     def minCut(self, s):
         """
         :type s: str
         :rtype: int
         """
         # acceleration
         if s == s[::-1]: return 0
         if any(s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1] for i in range(1, len(s))): return 1
         # algorithm
         cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
         for i in range(len(s)):
             r1, r2 = 0, 0
             # use i as origin, and gradually enlarge radius if a palindrome exists
             # odd palindrome
             while r1 <= i < len(s)-r1 and s[i-r1] == s[i+r1]:
                 cut[i+r1+1], r1 = min(cut[i+r1+1], cut[i-r1]+1), r1 + 1
             # even palindrome
             while r2 <= i < len(s)-r2-1 and s[i-r2] == s[i+r2+1]:
                 cut[i+r2+2], r2 = min(cut[i+r2+2], cut[i-r2]+1), r2 + 1
         return cut[-1]
