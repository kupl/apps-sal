n, m, x, y, z, p = list(map(int, input().split()))
x %= 4
y %= 2
z %= 4
tn, tm = n, m

while p >= 1:
    n, m = tn, tm
    p -= 1
    sx, sy = list(map(int, input().split()))
    for i in range(0, x):
        sx, sy = sy, n - sx + 1
        n, m = m, n
    if y > 0:
        sy = m - sy + 1
    for i in range(0, z):
        sx, sy = m - sy + 1, sx
        n, m = m, n
    print(sx, sy)
