n, m = list(map(int, input().split()))
tbl = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    c0 = 0
    c1 = 0
    for j in range(m):
        if tbl[i][j] == 0:
            c0 += 1
        else:
            c1 += 1
    ans += 2**c0 - 1
    ans += 2**c1 - 1
for i in range(m):
    c0 = 0
    c1 = 0
    for j in range(n):
        if tbl[j][i] == 0:
            c0 += 1
        else:
            c1 += 1
    ans += 2**c0 - 1
    ans += 2**c1 - 1
ans -= n * m
print(ans)
