n, m, x, y, z, p = map(int, input().split())
y = y % 2
x = x % 4
z = z % 4
 
for i in range(p):
    xi, yi = map(int, input().split())
    t = (n, m)
    for j in range(x):
        xi, yi = yi, n - xi + 1
        n, m = m, n
    if y == 1:
        yi = m - yi + 1
    for j in range((-z)%4):
        xi, yi = yi, n - xi + 1
        n, m = m, n
    n, m = t[0], t[1]
    print(xi, yi)
