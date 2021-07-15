from collections import deque
from collections import Counter
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
t = [[-1]*W for _ in range(H)]
q = deque([[0,0]])
t[0][0] = 0
while len(q) > 0:
  qq = q.popleft()
  dh = [-1,0,1,0]
  dw = [0,1,0,-1]
  for i in range(4):
    h = qq[0] + dh[i]
    w = qq[1] + dw[i]
    if 0 <= h < H and 0 <= w < W:
      if s[h][w] == "#" or t[h][w] != -1: continue
      t[h][w] = t[qq[0]][qq[1]] + 1
      q.append([h,w])

X = 0
for i in range(H):
  c = Counter(s[i])
  X += c["."]
if t[H-1][W-1] == -1:
  print(-1)
else:
  print(X-1-t[H-1][W-1])
