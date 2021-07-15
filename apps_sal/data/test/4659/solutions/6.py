class Solution:
     def generate(self, numRows):
         """
         :type numRows: int
         :rtype: List[List[int]]
         """
         A=[[1],[1,1]]
         if numRows == 0:
             return[]
         elif numRows<3:
             return A[0:numRows]
         else:
             i=3
             while i<=numRows:
                 temp=A[i-2][:]
                 temp.append(0)
                 temp2=temp[::-1]
                 temp3=[X+Y for X,Y in zip(temp,temp2)]
                 A.append(temp3) 
                 i+=1          
         print(A)
         return A
