n = int(input())
a = []
f = False
for i in range(n):
    a.append(input())
    if a[i][i] != a[i][n - 1 - i]:
        f = True
        break
c = a[0][1]
k = n // 2
if not f:
    if c == a[0][0] or a[k][k] != a[0][0]:
        f = True
    else:
        for i in range(n):
            for j in range(n):
                if i != j and j != n - 1 - i:
                    if a[i][j] != c:
                        f = True
                        break
            if f:
                break
if f:
    print('NO')
else:
    print('YES')
