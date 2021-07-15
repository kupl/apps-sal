import numpy as np
 
a,b=map(int,input().split())
A=np.array(sorted(list(map(int,input().split()))))
F=np.array(sorted(list(map(int,input().split())),reverse=True))
 
s=A.sum()
 
x=-1
y=10**12
while x+1<y:
  mid=(x+y)//2
  if s-np.minimum(A,mid//F).sum()<=b:
    y=mid
  else:
    x=mid
print(y)
