n, m, x, y, z, p = map(int, input().split())
x = x % 4
y = y % 2
z = z % 4
n0, m0 = n, m
for i in range(p):
    n, m = n0, m0
    x1, y1 = map(int, input().split())
    for j in range(x):
        x1, y1 = y1, n - x1 + 1
        n, m = m, n
    if y == 1:
        y1 = m - y1 + 1
    for i in range(z):
        x1, y1 = m - y1 + 1, x1
        n, m = m, n
    print(x1, y1)
