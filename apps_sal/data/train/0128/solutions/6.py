class Solution:
     def calculate(self, s):
         """
         :type s: str
         :rtype: int
         """
         expression = s
         s = []
         res = 0
         curr = 0
         sign = 1
         for c in expression:
             # print(c,res)
             if c.isdigit():
                 curr *= 10
                 curr += int(c)
             if c == "+":
                 res += sign * curr
                 curr = 0
                 sign = 1
             if c == "-":
                 res += sign * curr
                 curr = 0
                 sign = -1
             if c == "(":
                 s.append(res)
                 s.append(sign)
                 sign = 1
                 res = 0
             if c == ")":
                 res += sign * curr
                 curr = 0
                 res *= s.pop()
                 res += s.pop()
         
         if curr != 0:
             res += sign * curr
         return res
             
                 

