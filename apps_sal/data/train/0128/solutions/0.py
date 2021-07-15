class Solution:
     def calculate(self, s):
         """
         :type s: str
         :rtype: int
         """
         res = 0
         num = 0
         sign = 1
         stk = []
 
         for c in s:
             if c.isdigit():
                 num = 10 * num + (ord(c) - ord('0'))
             elif c == '+':
                 res += sign * num
                 num = 0
                 sign = 1
             elif c == '-':
                 res += sign * num
                 num = 0
                 sign = -1
             elif c == '(':
                 stk.append(res)
                 stk.append(sign)
                 res = 0
                 sign = 1
             elif c == ')':
                 res += sign * num
                 res *= stk.pop()
                 res += stk.pop()
                 num = 0
                 sign = 1
 
         if num:
             res += sign * num
         return res
