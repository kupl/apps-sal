N=int(input())
M=str(N)
a=[0]*len(M)
S=0
for i in range(len(M)):
  a[i]=int(M[i])
  
for j in a:
  S=S+j
  
if S%9==0:
  print("Yes")
else:
  print("No")
