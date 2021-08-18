import sys

[n, H] = list(map(int, sys.stdin.read().split()))

INF = 1000000000000000000000000000000


def tri(n): return n * (n + 1) // 2


def build(n, h):
    vol = tri(h)
    if h > H:
        r = h - H
        l = h - 1 - r
        sys.stderr.write("BUILD {} : {} {}\n".format(h, l, r))
        sys.stderr.write("LSIDE: {}\n".format(tri(l + r) - tri(l)))
        vol += tri(l + r) - tri(l)
        w = h + r
    else:
        w = h
    if vol > n:
        sys.stderr.write("BUILD {} -> NO WAY\n".format(h))
        return INF
    n -= vol
    w += n // h
    if n % h > 0:
        w += 1
    sys.stderr.write("BUILD {} -> {}\n".format(h, w))
    return w


l = 1
r = n
while l + 4 < r:
    sys.stderr.write("RANGE {}..{}\n".format(l, r))
    a = (l + l + r + 2) // 3
    b = (l + r + r + 2) // 3
    ay = build(n, a)
    by = build(n, b)
    if by == INF:
        r = b
        continue
    if ay < by:
        r = b
    else:
        l = a

ans = INF
for i in range(l, r + 1):
    ans = min(ans, build(n, i))

print(ans)
