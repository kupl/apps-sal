(n, m) = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    w = 0
    b = 0
    for j in range(m):
        if mat[i][j] == 1:
            w += 1
        else:
            b += 1
    ans += 2 ** w + 2 ** b - 2
for i in range(m):
    w = 0
    b = 0
    for j in range(n):
        if mat[j][i] == 1:
            w += 1
        else:
            b += 1
    ans += 2 ** w + 2 ** b - 2
print(ans - n * m)
