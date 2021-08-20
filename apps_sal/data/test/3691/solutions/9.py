import sys
lines = sys.stdin.readlines()
(x0, y0, ax, ay, bx, by) = list(map(int, lines[0].split()))
(xs, ys, t) = list(map(int, lines[1].split()))
x = [x0]
y = [y0]
for n in range(100):
    x.append(ax * x[-1] + bx)
    y.append(ay * y[-1] + by)
best = 0
for i in range(100):
    for j in range(100):
        d = abs(xs - x[j]) + abs(ys - y[j]) + abs(x[j] - x[i]) + abs(y[j] - y[i])
        if d <= t and j - i + 1 > best:
            best = abs(j - i) + 1
    for j in range(i + 1, 100):
        d = abs(xs - x[i]) + abs(ys - y[i]) + abs(x[i] - x[0]) + abs(y[i] - y[0]) + abs(x[j] - x[0]) + abs(y[j] - y[0])
        if d <= t and j + 1 > best:
            best = j + 1
print(best)
