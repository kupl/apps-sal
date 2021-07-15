#再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)

n,x=map(int,input().split())
a=[0]*(n+1)
p=[0]*(n+1)
a[0]=1
p[0]=1
for i in range(n):
  a[i+1]=2*a[i]+3
  p[i+1]=2*p[i]+1
  
def func(i,x):
  if i==0:
    if x<=0:
      return 0
    elif x>=1:
      return 1
  mid=(a[i]+1)//2
  if mid==x:
    return p[i-1]+1
  elif mid>x:
    return func(i-1,x-1)
  else:
    return p[i-1]+1+func(i-1,x-mid)


print(func(n,x))  
