def get_dist(cur, nxt):
    return abs(cur[0] - nxt[0]) + abs(cur[1] - nxt[1])


H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]

pos = {}
for i in range(H):
    for j in range(W):
        pos[A[i][j]] = (i, j)

acc = [0] * (H * W + 1)
for i in range(D + 1, H * W + 1):
    acc[i] = acc[i - D] + get_dist(pos[i - D], pos[i])

Q = int(input())
for _ in range(Q):
    ans = 0
    L, R = list(map(int, input().split()))
    print((acc[R] - acc[L]))

