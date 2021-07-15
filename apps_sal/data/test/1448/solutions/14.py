def make_line(x1, y1, x2, y2):
    b = (x1 * y2 - x2 * y1) / (x1 - x2)
    k = (y1 - y2) / (x1 - x2)
    return (k, b)


n, d = map(int, input().split())
k1, b1 = make_line(0, d, d, 0)
k2, b2 = make_line(0, d, n - d, n)
k3, b3 = make_line(n - d, n, n, n - d)
k4, b4 = make_line(n, n - d, d, 0)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    if y >= k1 * x + b1 and y <= k2 * x + b2 and y <= k3 * x + b3 and y >= k4 * x + b4:
        print('YES')
    else:
        print('NO')
