H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]

pos = [None] * (H * W)
for i in range(H):
    for j in range(W):
        pos[A[i][j] - 1] = (i, j)

d = [0] * (H * W)
for i in range(D, H * W):
    px, py = pos[i - D]
    x, y = pos[i]
    d[i] = d[i - D] + abs(x - px) + abs(y - py)

for l, r in LR:
    print(d[r - 1] - d[l - 1])
