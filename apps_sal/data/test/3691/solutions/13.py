(x0, y0, ax, ay, bx, by) = map(int, input().split())
(xs, ys, t) = map(int, input().split())
X = [(x0, y0)]
for i in range(100):
    (x, y) = X[-1]
    (x, y) = (ax * x + bx, ay * y + by)
    if x > 10 ** 18 or y >= 10 ** 18:
        break
    X.append((x, y))


def calc(l, r):
    if r >= len(X):
        return 0
    m = min(abs(xs - X[l][0]) + abs(ys - X[l][1]), abs(xs - X[r][0]) + abs(ys - X[r][1]))
    if m + sum([X[i + 1][0] - X[i][0] + X[i + 1][1] - X[i][1] for i in range(l, r)]) > t:
        return 0
    return r - l + 1


ma = 0
for l in range(100):
    for r in range(l, 100):
        ma = max(ma, calc(l, r))
print(ma)
