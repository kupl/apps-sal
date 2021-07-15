from collections import *
from copy import *
H,W = map(int,input().split())
S = [(W+2)*["#"]]+[["#"]+list(input())+["#"] for h in range(H)]+[(W+2)*["#"]]
D = [[1,0],[-1,0],[0,1],[0,-1]]
ans = 0
P = deque([])
Q = deque([])
 
for h in range(1,H+1):
  for w in range(1,W+1):
    if S[h][w]==".":
      P+=[[h,w]]
 
while P:
  T = deepcopy(S)
  sx,sy = P.popleft()
  T[sx][sy] = 0
  Q = deque([[sx,sy]])
  while Q:
    x,y = Q.popleft()
    for dx,dy in D:
      if T[x+dx][y+dy]==".":
        T[x+dx][y+dy] = T[x][y]+1
        Q+=[[x+dx,y+dy]]
        ans = max(ans,T[x+dx][y+dy])
 
print(ans)
