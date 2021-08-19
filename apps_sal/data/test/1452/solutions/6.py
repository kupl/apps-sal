(h, w) = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
mat = [None] * h
ans = 1
for i in range(h):
    mat[i] = [-1] * w
for i in range(h):
    for j in range(r[i]):
        mat[i][j] = 0
    if r[i] < w:
        mat[i][r[i]] = 1
for j in range(w):
    for i in range(c[j]):
        if mat[i][j] == 1:
            ans = 0
        mat[i][j] = 0
    if c[j] < h:
        if mat[c[j]][j] == 0:
            ans = 0
        mat[c[j]][j] = 1
for i in mat:
    for j in i:
        if j == -1:
            ans = 2 * ans % 1000000007
print(ans)
