from math import sin, pi
(n, r) = map(int, input().split())


def p(n, r):
    return 2 * n * r * sin(pi / n)


le = 0
ri = r * 1000
while ri - le > 1e-09:
    m = (ri + le) / 2
    if p(n, r + m) < n * m * 2:
        ri = m
    else:
        le = m
print(m)
