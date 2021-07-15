class Solution:
     def generateParenthesis(self, n):
         """
         :type n: int
         :rtype: List[str]
         """
         rst = []
         cake = ''
         self.generateRecursion(rst,cake,n,n)
         return rst
     def generateRecursion(self,rst,cake,left,right):
         if right==0:
             rst.append(cake)
         if left>0:
             self.generateRecursion(rst,cake+'(',left-1,right)
         if right>left:
             self.generateRecursion(rst,cake+')',left,right-1)

