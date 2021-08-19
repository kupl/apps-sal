from sys import stdin


def rd():
    return list(map(int, input().split()))


def g(x, i):
    return x.get(i, 0)


(n, a, b) = rd()
(c, d) = ({}, {})
r = 0
for z in range(n):
    (_, x, y) = rd()
    (i, j) = (a * x - y, (x, y))
    r += g(c, i) - g(d, j)
    c[i] = g(c, i) + 1
    d[j] = g(d, j) + 1
print(2 * r)
