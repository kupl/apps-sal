class Solution:
     def numDecodings(self, s):
         """
         :type s: str
         :rtype: int
         """
         if not s:
             return 0
         
         def num_decode(i):
             # Number of ways to decode s[i:]
             if i == len(s):
                 return 1
 
                 
             if i not in memo:                
                 num_ways = 0
                 
                 if s[i] in single_digit_codes:
                     num_ways += num_decode(i + 1)
 
                 if s[i:i+2] in double_digit_codes:
                     num_ways += num_decode(i + 2)
             
                 memo[i] = num_ways
             return memo[i]
         single_digit_codes = set(str(x) for x in range(1, 10))
         double_digit_codes = set(str(x) for x in range(10, 27))
         memo = {}
         return num_decode(0)
