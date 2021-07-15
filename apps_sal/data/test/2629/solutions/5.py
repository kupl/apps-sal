class Solution:
     def generateMatrix(self, n):
         """
         :type n: int
         :rtype: List[List[int]]
         """
         t=1
         temp=[]
         for i in range(n):
         	temp.append([None]*n)
         rep = int(n/2) if n%2==0 else int(n/2)+1
         k=1
 
         for i in range(rep):
         	for j in range(i,n-i-1):
         		temp[i][j] = k
         		k+=1
         	for j in range(i,n-i-1):
         		temp[j][n-i-1] = k
         		k+=1
         	for j in range(n-i-1,i,-1):
         		temp[n-i-1][j] = k
         		k+=1
         	for j in range(n-i-1,i,-1):
         		temp[j][i] = k
         		k+=1
         if n%2==1:temp[int(n/2)][int(n/2)]=n*n
         return temp        
