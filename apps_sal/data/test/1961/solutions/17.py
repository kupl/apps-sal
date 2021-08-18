n, m = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(list(map(str, input().strip())))
t = []
for i in range(n):
    p = ['.'] * m
    t.append(p)

for i in range(1, n - 1):
    for j in range(1, m - 1):
        f = 0
        if s[i - 1][j - 1] == '
        f = 1
        if f == 1:
            t[i - 1][j - 1] = '
            t[i - 1][j] = '
            t[i - 1][j + 1] = '
            t[i][j - 1] = '
            t[i][j + 1] = '
            t[i + 1][j - 1] = '
            t[i + 1][j] = '
            t[i + 1][j + 1] = '
f = 1
for i in range(n):
    for j in range(m):
        if s[i][j] == '
        f = 0
        break
    if f == 0:
        break
if f == 1:
    print("YES")
else:
    print("NO")
