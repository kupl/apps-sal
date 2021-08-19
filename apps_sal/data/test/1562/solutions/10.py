from bisect import bisect_left
(n, m, k, q) = list(map(int, input().split()))
x = sorted((list(map(int, input().split())) for _ in range(k)))
y = sorted(map(int, input().split()))


def rr(c0, c1, c):
    return abs(c0 - c) + abs(c1 - c)


def tm(c0, c1):
    t = bisect_left(y, c0)
    tt = []
    if t > 0:
        tt.append(rr(c0, c1, y[t - 1]))
    if t < q:
        tt.append(rr(c0, c1, y[t]))
    return min(tt)


z = []
for (r, c) in x:
    if z and z[-1][0] == r:
        z[-1][2] = c
    else:
        z.append([r, c, c])
(v1, v2, r0, c01, c02) = (0, 0, 1, 1, 1)
for (r1, c11, c12) in z:
    d = c12 - c11 + r1 - r0
    if r1 > r0:
        d11 = tm(c01, c11)
        d12 = tm(c01, c12)
        d21 = tm(c02, c11)
        d22 = tm(c02, c12)
        (v2, v1) = (d + min(v1 + d11, v2 + d21), d + min(v1 + d12, v2 + d22))
    else:
        (v1, v2) = (d + c12 - c02, d + c11 - c01)
    (r0, c01, c02) = (r1, c11, c12)
print(min(v1, v2))
