import copy
import heapq
from collections import deque
n=int(input())
left=[]
middle=deque([])
right=[]
A=list(map(int,input().split()))
for i in range(n):
  heapq.heappush(left,A[i])
c=sum(left)
for i in range(n):
  middle.append(A[n+i])
for i in range(n):
  heapq.heappush(right,A[2*n+i]*-1)
d=sum(right)
l=deque([0])
m=copy.copy(middle)
for i in range(n):
  a=left[0]
  b=m[0]
  l.append(l[-1]+max(0,b-a))
  if b-a>0:
    heapq.heapreplace(left,b)
  m.popleft()
m=copy.copy(middle)
r=deque([0])
for i in range(n):
  a=right[0]*-1
  b=m[-1]
  r.append(r[-1]+max(0,a-b))
  if a-b>0:
    heapq.heapreplace(right,b*-1)
  m.pop()
ans=0
for i in range(n+1):
  a=l[0]+r[-1]
  if a>ans:
    ans=a
  l.popleft()
  r.pop()
print(c+d+ans)
