from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import deque

n,m=nii()

tree=[[] for i in range(n)]
for i in range(m):
  a,b=nii()
  a-=1
  b-=1
  tree[a].append(b)
  tree[b].append(a)

ans=[-1 for i in range(n)]
ans[0]=1

que=deque()
que.append(0)

while que:
  x=que.popleft()
  for i in tree[x]:
    if ans[i]==-1:
      ans[i]=x
      que.append(i)

if -1 in ans:
  print('No')
else:
  print('Yes')
  for i in ans[1:]:
    print(i+1)
