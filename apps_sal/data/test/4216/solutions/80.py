from math import *

def func(x):
  ret_val=0
  while 0<x:
    x//=10
    ret_val+=1
  return ret_val

N=int(input())
ans=func(N)
for A in range(1,int(sqrt(N))+1):
  if N%A==0:
    B=N//A
    temp=max(func(A),func(B));
    ans=min(ans,temp)
print(ans)

