H, W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))
c = [[None]*W for _ in range(H)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
i,j = 0,0
d = 0
color = 0
for _ in range(H*W):
    c[i][j] = color+1
    a[color] -= 1
    if a[color] == 0:
        color += 1
    di,dj = dirs[d]
    ni,nj = i+di,j+dj
    if 0 <= ni < H and 0 <= nj < W and c[ni][nj] == None:
        i,j = ni,nj
        continue
    d = (d+1) % 4
    di,dj = dirs[d]
    i,j = i+di,j+dj
for l in c:
    print(*l)
