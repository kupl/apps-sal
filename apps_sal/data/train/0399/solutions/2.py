class Solution:
     def numDecodings(self, s):
         """
         :type s: str
         :rtype: int
         """ 
         if s == None or len(s) == 0:
             return 0
             
         def in10(c):
             return c.isdigit() and c>'0' and c<='9'
         def in26(c):
             return c.isdigit() and c>='10' and c<='26'
         
         
         memo = [0 for _ in range(len(s))]
         if in10(s[0]):
             memo[0] = 1 
         
         for i in range(1, len(s)):
             if i == 1:
                 if in10(s[i]):
                     memo[i] = memo[i-1]
                 if in26(s[:2]):
                     memo[i] = memo[i] + 1
             else:
                 if in10(s[i]):
                     memo[i] += memo[i-1]
                 if in26(s[i-1:i+1]):
                     memo[i] += memo[i-2]
                     
         
         return memo[-1]
             
             
         
         

