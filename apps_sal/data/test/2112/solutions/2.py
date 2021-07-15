import sys
n,m=map(int,input().split())
x,k,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if k*y<x:
  ycheap=1
else:
  ycheap=0
pointer=0
ans=0
for i in range(m):
  deletenum=0
  badnum=0
  if pointer==n:
    print(-1)
    return
  start=pointer
  deletnum=0
  while a[pointer]!=b[i]:
    if (i==0 and b[0]<a[pointer]) or (i>0 and b[i]<a[pointer] and b[i-1]<a[pointer]):
      badnum=1
    pointer+=1
    deletenum+=1
    if pointer==n:
      print(-1)
      return
  pointer+=1
  if badnum==1 and deletenum<k:
    print(-1)
    return
  if ycheap==1:
    if badnum==1:
      ans+=x
      ans+=y*(deletenum-k)
    else:
      ans+=y*deletenum
  else:
    ans+=y*(deletenum%k)
    ans+=x*(deletenum//k)
badnum=0
for i in range(pointer,n):
  if a[i]>b[-1]:
    badnum=1
deletenum=n-pointer
if badnum==1 and deletenum<k:
  print(-1)
  return
if ycheap==1:
  if badnum==1:
    ans+=x
    ans+=y*(deletenum-k)
  else:
    ans+=y*deletenum
else:
  ans+=y*(deletenum%k)
  ans+=x*(deletenum//k)
print(ans)
