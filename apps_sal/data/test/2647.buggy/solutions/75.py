import sys
(H, W) = list(map(int, input().split()))
sx = 0
sy = 0
gx = W - 1
gy = H - 1
ans = 0
A = [list((i for i in input())) for _ in range(H)]
for j in A:
    ans += j.count('.')
inf = -1
distance = [[inf] * W for _ in range(H)]
queue = []
queue.insert(0, (sy, sx))
distance[sy][sx] = 0
X = 0
while True:
    try:
        (y, x) = queue.pop()
    except:
        break
    for i in range(4):
        nx = x + (-1, 0, 1, 0)[i]
        ny = y + (0, -1, 0, 1)[i]
        if 0 <= nx and nx <= W - 1 and (0 <= ny) and (ny <= H - 1) and (A[ny][nx] != '#') and (distance[ny][nx] == inf):
            queue.insert(0, (ny, nx))
            distance[ny][nx] = distance[y][x] + 1
            A[ny][nx] = '!'
if distance[H - 1][W - 1] != inf:
    ans -= distance[gy][gx] + 1
    print(ans)
else:
    print(-1)
