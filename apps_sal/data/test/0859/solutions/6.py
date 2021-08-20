def fac(n):
    ret = 1
    for i in range(2, n):
        ret *= i
    return ret


def C(n, k):
    return fac(n) // fac(k) // fac(n - k)


def transform(s):
    res = 0
    for c in s:
        if c == '0':
            res += 1
        else:
            res -= 1
    return res


s1 = input().strip()
s2 = input().strip()
dx = sum([1 if c == '+' else -1 for c in s1])
u = 0
dx2 = 0
for c in s2:
    if c == '?':
        u += 1
    else:
        dx2 += 1 if c == '+' else -1
if u == 0:
    if dx == dx2:
        print(1)
    else:
        print(0)
elif abs(dx - dx2) > u:
    print(0)
else:
    d = abs(dx - dx2)
    well = 0
    for i in range(1 << u):
        if transform(bin(i)[2:].rjust(u, '0')) == d:
            well += 1
    print(well / (1 << u))
