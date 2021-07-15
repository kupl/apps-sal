H,W = map(int,input().split())
s = [input() for i in range(H)]
from collections import deque
m = [[-1]*W for i in range(H)]
m[0][0] = 0
d = deque()
d.append([0,0])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while len(d) > 0:
    y,x = d.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny <= H-1 and 0 <= nx <= W-1 and s[ny][nx] == "." and m[ny][nx] == -1:
            m[ny][nx] = m[y][x] + 1
            d.append([ny,nx])
ans = m[H-1][W-1]
whites = -1
for i in s:
    whites += i.count(".")
if ans != -1:
    ans = whites - ans
print(ans)
