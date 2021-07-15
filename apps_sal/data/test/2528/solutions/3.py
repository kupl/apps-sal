def solve(A):
 
 
 count = 0
 i = 0
 n = len(A)
 while (i<n and A[i] == 0):
  i+=1
 if i<n and A[i]!=0:
  maxi = 1
 else:
  maxi = 0
 while (i<n):
  
  if A[i]>0:
   count+=1
   
   maxi = max(maxi,count)
   
  else:
   maxi = max(maxi,count)
   count = 0
   
  i+=1
   
  
 return maxi

n = int(input())
A= list(map(int,input().split()))
print(solve(A))
