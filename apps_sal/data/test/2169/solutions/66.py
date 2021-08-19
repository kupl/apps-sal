from itertools import accumulate


def get_dist(cur, nxt):
    return abs(cur[0] - nxt[0]) + abs(cur[1] - nxt[1])


(H, W, D) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
pos = {}
for i in range(H):
    for j in range(W):
        pos[A[i][j] - 1] = (i, j)
acc = []
for i in range(D):
    res = [0]
    now = i
    while now + D < H * W:
        nxt = now + D
        res.append(get_dist(pos[now], pos[nxt]))
        now = nxt
    acc.append(list(accumulate(res)))
Q = int(input())
for _ in range(Q):
    ans = 0
    (L, R) = list(map(int, input().split()))
    L -= 1
    R -= 1
    path = acc[L % D]
    print(path[R // D] - path[L // D])
