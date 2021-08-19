(N, C) = list(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(C)]
color = [list(map(int, input().split())) for _ in range(N)]
cs = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        amari = (i + j) % 3
        cs[amari][color[i][j] - 1] += 1
ans = 500 * 500 * 1000
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            now = 0
            for ci in range(C):
                now += D[ci][i] * cs[0][ci]
                now += D[ci][j] * cs[1][ci]
                now += D[ci][k] * cs[2][ci]
            ans = min(ans, now)
print(ans)
