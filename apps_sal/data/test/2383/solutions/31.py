import math
n=int(input())
A=list(map(int,input().split()))
num=1
brk=0
for i in range(n):
  if A[i]==num:
    num+=1
  else:
    brk+=1

if num==1 and brk!=0:
  print(-1)
else:
  print(brk)
