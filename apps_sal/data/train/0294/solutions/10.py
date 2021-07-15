class Solution:
     def totalNQueens(self, n):
         """
         :type n: int
         :rtype: int
         """
         row = [x for x in range(n)]
         table = []
         for i in range(n):
             table.append(row.copy())
         result = self.solve(table,0)
         return len(result)
     def solve(self,table,n):
         if table[n]==[]:return []
         elif n==len(table)-1:
             table[n] = table[n][0]
             return [table]
         else:
             result=[]
             for x in table[n]:
                 table1 = [(x if type(x)==int else x.copy()) for x in table]
                 table1[n] = x
                 for row in range(n+1,len(table)):
                     if x in table1[row]:
                         table1[row].remove(x)
                     if x+row-n in table1[row]:
                         table1[row].remove(x+row-n)
                     if x-(row-n) in table1[row]:
                         table1[row].remove(x-(row-n))
                 result.extend(self.solve(table1,n+1))
             return result
