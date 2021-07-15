import sys
input = sys.stdin.readline
from heapq import heapify,heappush,heappop
t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  ab = [list(map(int,input().split())) for i in range(m)]
  go = [[] for i in range(n+1)]
  come = [[] for i in range(n+1)]
  for a,b in ab:
    go[a].append(b)
    come[b].append(a)
  exist = [1]*(n+1)
  flg = [10]*(n+1)
  for i in range(1,n+1):
    if flg[i] == 10:
      flg[i] = 2
    if flg[i] == 0:
      exist[i] = 0
    if go[i]:
      if flg[i] == 0:
        for j in go[i]:
          flg[j] = min(flg[j],2)
      else:
        for j in go[i]:
          flg[j] = min(flg[j],flg[i]-1)
  print(exist.count(0))
  ansls = []
  for i in range(1,n+1):
    if exist[i] == 0:
      ansls.append(i)
  print(*ansls)
