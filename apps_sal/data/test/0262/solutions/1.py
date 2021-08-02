n = int(input())
s = -1
s1 = -1
x = -1
y = -1
mat = []
if n == 1:
    input()
    print(1)
    return
for i in range(n):
    arr = list(map(int, input().split()))
    if s == -1 and 0 not in arr:
        s = sum(arr)
    if 0 in arr:
        x = i
        s1 = sum(arr)
        y = arr.index(0)
    mat.append(arr)
mat[x][y] = s - s1
if mat[x][y] <= 0:
    print(-1)
    return
for i in range(n):
    if sum(mat[i]) != s:
        print(-1)
        return
    s2 = 0
    for j in range(n):
        s2 += mat[j][i]
    if s2 != s:
        print(-1)
        return
s2 = 0
s3 = 0
for i in range(n):
    s2 += mat[i][i]
    s3 += mat[i][n - i - 1]
if s2 != s or s3 != s:
    print(-1)
    return
print(mat[x][y])
