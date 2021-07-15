import numpy as np
N=int(input())
A=list(map(int,input().split()))
A=np.array(A)

count=0
flag=True
while flag:
  for i in range(N):
    if A[i]%2==1:
      flag=False
  A=A/2
  if flag:
    count+=1
print(count)
