from math import sqrt
(ax, ay, bx, by, tx, ty) = map(int, input().split())
n = int(input())
ans = 0
(p1, p2, beg, end) = ([0] * n, [0] * n, [0] * n, [0] * n)


def sqr(x):
    return x * x


def pref(x):
    return beg[x] if x >= 0 else 0


def suff(x):
    return end[x] if x < n else 0


def ex(x):
    return max(pref(x - 1), suff(x + 1))


for i in range(n):
    (x, y) = map(int, input().split())
    d = sqrt(sqr(x - tx) + sqr(y - ty))
    d1 = sqrt(sqr(x - ax) + sqr(y - ay))
    d2 = sqrt(sqr(x - bx) + sqr(y - by))
    ans += d + d
    (p1[i], p2[i]) = (d - d1, d - d2)
beg[0] = p1[0]
for i in range(1, n):
    beg[i] = max(beg[i - 1], p1[i])
end[n - 1] = p1[n - 1]
for i in range(n - 2, -1, -1):
    end[i] = max(end[i + 1], p1[i])
res = 1e+220
for i in range(0, n):
    res = min(res, min(ans - p2[i] - ex(i), ans - max(p1[i], p2[i])))
print(res)
