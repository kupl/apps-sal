#import math
import collections
n, m = map(int, input().split( ))
lis = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split( ))
  lis[a].append(b)
  lis[b].append(a)
#print(lis)
ans = [0]*(n+1)
q = collections.deque()
q.append(1)
count = [0]*(n+1)
#1の時は動かない
count[1] = 1
while len(q) != 0:
  v = q.popleft()
#  print(lis[v], count)
  #まずは1につながっている部屋を探索その後順に探索
  for u in lis[v]:
    if count[u] == 0:
      count[u] = 1
      ans[u] = v
      q.append(u)
print('Yes')
for i in range(2,n+1):
  print(ans[i])
