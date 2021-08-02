n, x1, y1, x2, y2 = list(map(int, input().split()))
l = [(0, 0)]
for i in range(n):
    X, Y = list(map(int, input().split()))
    l += [((X - x1)**2 + (Y - y1)**2, (X - x2)**2 + (Y - y2)**2)]
l = sorted(l)
a = 10000000000000000
Y = a
for i in range(n + 1):
    x, y = l[i][0], 0
    for j in range(i + 1, n + 1):
        if l[j][0] > x:
            y = max(y, l[j][1])
    a = min(a, x + y)
print(a)
