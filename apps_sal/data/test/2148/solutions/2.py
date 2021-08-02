from math import sqrt
n, r = list(map(int, input().split()))
x = list(map(int, input().split()))
y = []
for i in range(n):
    y.append(r)
    for j in range(i):
        d = abs(x[i] - x[j])
        if d > 2 * r:
            continue
        inc = sqrt(4 * r * r - d * d)
        y[i] = max(y[i], y[j] + inc)
print(' '.join(map(str, y)))
