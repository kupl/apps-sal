class Solution:
     def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         
         self.mem = {}
         self.t = s
         self.p = p
         
         return self.match(0,0)
     
     def match(self, i, j):
         
         if (i,j) not in self.mem:
             if j == len(self.p):
                 res = i == len(self.t)
                 
             else:
                 if j+1 < len(self.p) and self.p[j+1] == '*':
                     res = self.match(i, j+2) or (i < len(self.t) and self.p[j] in {self.t[i], '.'} and self.match(i+1, j))
                 else:
                     res = i < len(self.t) and self.p[j] in {self.t[i], '.'} and self.match(i+1, j+1)
                     
             self.mem[i, j] = res
                 
         return self.mem[i, j]
         

