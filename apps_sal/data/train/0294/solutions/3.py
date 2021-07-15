class Solution:
     def totalNQueens(self, n):
         """
         :type n: int
         :rtype: int
         """
         rl=[0]
         col=[False for x in range(n)]
         dia1=[False for x in range(2*n-1)]
         dia2=[False for x in range(2*n-1)]
         self.putQueen(n,col,dia1,dia2,rl,0)
         return rl[0]
     
     def putQueen(self,n,col,dia1,dia2,rl,index):
         if index==n:
             rl[0]+=1
             return True
         for i in range(n):
             if not col[i] and not dia1[index+i] and not dia2[index-i+n-1]:
                 col[i]=True
                 dia1[index+i]=True
                 dia2[index-i+n-1]=True
                 self.putQueen(n,col,dia1,dia2,rl,index+1)
                 col[i]=False
                 dia1[index+i]=False
                 dia2[index-i+n-1]=False
