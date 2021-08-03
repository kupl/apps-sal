N, C = list(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

cst = [[0, 0, 0] for i in range(C)]

for i in range(N):
    for j in range(N):
        cst[c[i][j] - 1][(i + j) % 3] += 1

ans = 10**10

for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or i == k or j == k:
                continue
            x = [i, j, k]
            a = 0
            for l in range(3):
                for m in range(C):
                    a += D[m][x[l]] * cst[m][l]
            ans = min(ans, a)

print(ans)
