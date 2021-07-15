class Solution:
     def checkValidString(self, s):
         """
         :type s: str
         :rtype: bool
         """
         l = r = star = 0
         
         for c in s:
             if c == "(":
                 l+=1
             if c == ")":
                 r+=1
             if c == "*":
                 star+=1
             if r > star + l:
                 return False
             
         l = r = star = 0
         
         for c in s[::-1]:
             if c == "(":
                 l +=1
             if c == ")":
                 r +=1
             if c == "*":
                 star +=1
             if l > star + r:
                 return False
         return True
