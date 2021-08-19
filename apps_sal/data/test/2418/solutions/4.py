import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
d = []
b = 0
c = 0
F = a[0]
L = a[-1]
for i in range(1, n):
    x = a[i] - a[i - 1]
    if x >= 0:
        b = b + x
    else:
        c = c - x
    d.append(x)
Q = int(sys.stdin.readline().strip())
for q in range(0, Q + 1):
    if q > 0:
        (l, r, x) = list(map(int, sys.stdin.readline().strip().split()))
    else:
        (l, r, x) = (1, 1, 0)
    if x != 0 and l > 1:
        if x >= 0 and d[l - 2] >= 0:
            b = b + x
        elif x >= 0 and d[l - 2] < 0:
            b = b + x - min(-d[l - 2], x)
            c = c - min(-d[l - 2], x)
        elif x < 0 and d[l - 2] >= 0:
            c = c - min(d[l - 2], -x) - x
            b = b - min(d[l - 2], -x)
        elif x < 0 and d[l - 2] < 0:
            c = c - x
        d[l - 2] = d[l - 2] + x
    elif x != 0 and l == 1:
        F = F + x
    if x != 0 and r < n:
        if x <= 0 and d[r - 1] >= 0:
            b = b - x
        elif x <= 0 and d[r - 1] < 0:
            b = b - x - min(-x, -d[r - 1])
            c = c - min(-x, -d[r - 1])
        elif x > 0 and d[r - 1] >= 0:
            c = c - min(x, d[r - 1]) + x
            b = b - min(x, d[r - 1])
        elif x > 0 and d[r - 1] < 0:
            c = c + x
        d[r - 1] = d[r - 1] - x
    elif x != 0 and r == n:
        L = L + x
    print((L + F + b + c + 3) // 4)
