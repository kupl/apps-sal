from collections import *
H,W = map(int,input().split())
S = [input() for h in range(H)]
V = [W*[0] for h in range(H)]
V[0][0] = 1
Q = deque([(0,0)])
while Q:
  x,y = Q.popleft()
  for dx,dy in ((-1,0),(0,-1),(1,0),(0,1)):
    if 0<=x+dx<H and 0<=y+dy<W and V[x+dx][y+dy]==0 and S[x+dx][y+dy]==".":
      V[x+dx][y+dy] = V[x][y]+1
      Q.append((x+dx,y+dy))

if V[H-1][W-1]==0:
  print(-1)
else:
  print(H*W-sum(s.count("#") for s in S)-V[H-1][W-1])
