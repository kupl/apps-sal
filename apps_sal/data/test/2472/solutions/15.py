import numpy as np
n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
  a[i],b[i]=map(int,input().split())

flag=True
sum=0
sorted_index=np.argsort(b)
for i in sorted_index:
  sum+=a[i]
  if sum>b[i]:
    flag=False
    break
    
if flag:
  print('Yes')
else:
  print('No')
