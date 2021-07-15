class Solution:
     def calculate(self, s):
         """
         :type s: str
         :rtype: int
         """
         sign=[1]
         nums=0
         total=0
         latestsign=1
         for c in s:
             
             if c.isdigit():
                 nums=10*nums+int(c)
             elif c=='(':
                 nums=0
                 sign.append(latestsign)
             elif c==')':
                 total=total+latestsign*nums
                 sign.pop()
                 nums=0
             elif c in ['+','-']:
                 total=total+latestsign*nums
                 latestsign=sign[-1]*(+1 if c=='+' else -1)
                 nums=0
         
         return total+latestsign*nums
