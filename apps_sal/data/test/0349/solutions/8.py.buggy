n, m = [int(x) for x in input().split()]
a = []
b = []
for i in range(n):
    c = [int(x) for x in input().split()]
    a.append(c)
for i in range(n):
    c = [int(x) for x in input().split()]
    b.append(c)
for i in range(n):
    for j in range(m):
        x, y = a[i][j], b[i][j]
        a[i][j] = min(x, y)
        b[i][j] = max(x, y)
        if j > 0:
            if a[i][j] <= a[i][j - 1] or b[i][j] <= b[i][j - 1]:
                print('Impossible')
                return
        if i > 0:
            if a[i][j] <= a[i - 1][j] or b[i][j] <= b[i - 1][j]:
                print('Impossible')
                return
print('Possible')
