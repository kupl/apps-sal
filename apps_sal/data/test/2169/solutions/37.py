import sys
readline = sys.stdin.readline

H, W, D = list(map(int, readline().split()))

route = [0] * (H * W + 1)
for i in range(H):
    line = list(map(int, readline().split()))
    for j in range(len(line)):
        route[line[j]] = (i, j)

# 1,2,3 ... の頂点番号を格納した配列を作る
# D個おきに距離を格納する

dist = [0] * (H * W + 1)
for i in range(D + 1, len(route)):
    gy, gx = route[i]
    sy, sx = route[i - D]
    dist[i] = abs(gy - sy) + abs(gx - sx)
    dist[i] = dist[i] + dist[i - D]


Q = int(readline())

for i in range(Q):
    l, r = list(map(int, readline().split()))
    print((dist[r] - dist[l]))
