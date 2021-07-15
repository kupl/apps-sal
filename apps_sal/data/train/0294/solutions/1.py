class Solution:
     def totalNQueens(self, n):
         """
         :type n: int
         :rtype: int
         """
         result=[]
         self.DFS(n,0,"",[],[],[],result)
         print(result)
         return len(result) 
             
     def DFS(self, n, row, sss, check_col,check_diag1,check_diag2, result):
         """ sss is solution string, all other checks are checks for occupied places """
         if (len(sss) == n):
             result.append('.')
             return
         
         for col in range(0,n):
             if (col in check_col): continue
             if (row+col in check_diag1): continue
             if (row-col in check_diag2): continue
             self.DFS(n, row+1, sss+str(col), check_col+[col], 
                  check_diag1+[row+col], check_diag2+[row-col],result)
