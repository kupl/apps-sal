N, C = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(C)]

g0 = [0] * C
g1 = [0] * C
g2 = [0] * C


for i in range(N):
    col = list(map(int, input().split()))
    for j in range(N):
        col[j] -= 1
        if (i + j) % 3 == 0:
            g0[col[j]] += 1
        elif (i + j) % 3 == 1:
            g1[col[j]] += 1
        else:
            g2[col[j]] += 1

ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or i == k:
                continue
            s = 0
            for l in range(C):
                s += d[l][i] * g0[l] + d[l][j] * g1[l] + d[l][k] * g2[l]
            ans = min(ans, s)
print(ans)
