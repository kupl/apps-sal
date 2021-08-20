(N, M) = map(int, input().split())
c = [list(map(int, input().split())) for i in range(N)]
bit = [[] for i in range(2 ** 3)]
for k in range(N):
    for i in range(2 ** 3):
        t = c[k].copy()
        for j in range(3):
            if i >> j & 1:
                t[j] *= -1
        bit[i].append(t)
for i in range(2 ** 3):
    bit[i].sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
res = 0
for i in range(2 ** 3):
    p = [1, 1, 1]
    for j in range(3):
        if i >> j & 1:
            p[j] *= -1
    (z, o, t) = (0, 0, 0)
    for k in range(M):
        z += bit[i][k][0] * p[0]
        o += bit[i][k][1] * p[1]
        t += bit[i][k][2] * p[2]
    res = max(res, abs(z) + abs(o) + abs(t))
print(res)
