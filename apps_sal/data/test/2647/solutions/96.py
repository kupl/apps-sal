H,W = map(int,input().split())
s = ['' for i in range(H)]
white = H*W
black = 0
for i in range(H):
    s[i] = input()
    black += s[i].count('#')
white -= black
direction = [[1,0],[0,1],[-1,0],[0,-1]]
q = [[0,0,0]]

mass = [[-1 for i in range(W)] for j in range(H)]
while len(q) > 0:
    tmp = [y,x,d] = q.pop(0)
    if mass[y][x] >= 0: 
        continue
    mass[y][x] = d
    for [dy,dx] in direction:
        ny = y + dy
        nx = x + dx
        if 0 <= ny and ny < H and 0 <= nx and nx < W:
            if s[ny][nx] == '#' or mass[ny][nx] >= 0:
                continue
            q.append([ny,nx,d+1])
# for i in mass:
#     print(i)
if mass[H-1][W-1] < 0:
    print(-1)
else:
    print(white - mass[H-1][W-1] - 1)
