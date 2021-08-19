(n, c) = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
g0 = [0] * c
g1 = [0] * c
g2 = [0] * c
for i in range(n):
    col = list(map(int, input().split()))
    for j in range(n):
        col[j] -= 1
        if (i + j) % 3 == 0:
            g0[col[j]] += 1
        elif (i + j) % 3 == 1:
            g1[col[j]] += 1
        else:
            g2[col[j]] += 1
ans = 10 ** 18
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i == j or j == k or i == k:
                continue
            s = 0
            for l in range(c):
                s += d[l][i] * g0[l] + d[l][j] * g1[l] + d[l][k] * g2[l]
            ans = min(ans, s)
print(ans)
