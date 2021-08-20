(n, m, x, y, z, p) = map(int, input().split())
ps = []
for i in range(p):
    ps.append(list(map(int, input().split())))
x = x % 4
y = y % 2
z = z % 4 * 3 % 4
for p in ps:
    (mm, nn) = (m, n)
    (i, j) = p
    for _ in range(x):
        (i, j) = (j, nn - i + 1)
        (mm, nn) = (nn, mm)
    for _ in range(y):
        (i, j) = (i, mm - j + 1)
    for _ in range(z):
        (i, j) = (j, nn - i + 1)
        (mm, nn) = (nn, mm)
    print(i, j)
