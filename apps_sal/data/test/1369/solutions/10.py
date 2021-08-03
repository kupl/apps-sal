from itertools import combinations
N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]
a = 9999


def f(X, Y, R2, a):
    if all([(X - x)**2 + (Y - y)**2 < R2 for x, y in XY]):
        a = min(a, R2**.5)
    return a


for (x1, y1), (x2, y2), (x3, y3) in combinations(XY, 3):
    e1 = (x2 - x3)**2 + (y2 - y3)**2
    e2 = (x3 - x1)**2 + (y3 - y1)**2
    e3 = (x1 - x2)**2 + (y1 - y2)**2
    p = e1 * (e2 + e3 - e1)
    q = e2 * (e3 + e1 - e2)
    r = e3 * (e1 + e2 - e3)
    if p + q + r == 0:
        continue
    X = (p * x1 + q * x2 + r * x3) / (p + q + r)
    Y = (p * y1 + q * y2 + r * y3) / (p + q + r)
    R2 = (X - x1)**2 + (Y - y1)**2 + 10e-9
    a = f(X, Y, R2, a)
for (x1, y1), (x2, y2) in combinations(XY, 2):
    X = (x1 + x2) / 2
    Y = (y1 + y2) / 2
    R2 = (X - x1)**2 + (Y - y1)**2 + 10e-9
    a = f(X, Y, R2, a)
print(a)
