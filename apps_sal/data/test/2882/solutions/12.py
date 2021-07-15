class Solution:
     def parenthesis(self, n):
         return "("*n+")"*n
     
     def generateParenthesis(self, n):
         """
         :type n: int
         :rtype: List[str]
         """
         if n == 0:
             return []
         elif n == 1:
             return ["()"]
         
         result = []
         for i in range(1,n):
             r1 = self.generateParenthesis(i)
             r2 = self.generateParenthesis(n-i)
             for r11 in r1:
                 for r21 in r2:
                     result.append(r11+r21)
                     
         r3 = self.generateParenthesis(n-1)
         for r31 in r3:
             result.append("({})".format(r31))
         
         result.sort()
         rr = []
         last = None
         for r in result:
             if r == last:
                 continue
             rr.append(r)
             last = r
             
                 
         return rr

