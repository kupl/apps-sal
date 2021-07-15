# coding: utf-8
# Your code here!
N=int(input())
A=list(int(x) for x in input().split())

A.sort(reverse=True)

ans=0
for i in range(N):
  a=A[i]
  if i%2==0:
    ans += a
  else:
    ans -= a
  
print(ans)

