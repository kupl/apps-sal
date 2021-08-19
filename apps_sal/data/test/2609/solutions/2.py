import sys
from math import gcd


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    a = [None] * (2 * n)
    c = [0] * (2 * n)
    for i in range(0, 2 * n, 2):
        l, r = mints()
        a[i] = (l * 2, 0, i)
        a[i + 1] = (r * 2 + 1, 1, i)
        c[i + 1] = (l * 2, r * 2 + 1)
    a.sort()
    # print(a)
    s = set()
    p = None
    start = None
    px = int(-2e9 - 5)  # prev event
    pt = -1
    pp = px
    segs = []
    for i in range(0, 2 * n):
        x, t, id = a[i]
        if px != x:
            # print(px,x)
            cd = len(s)
            if cd == 1:
                segs.append((px, x, cd, next(iter(s))))
            else:
                segs.append((px, x, cd, None))
            px = x
        if t == 0:
            s.add(id)
        else:
            s.remove(id)
    segs.append((px, int(2e9 + 5), 0, None))
    res = 0
    p = False
    for i in range(1, len(segs) - 1):
        px, x, cd, e = segs[i]
        if e != None:
            l, r = c[e + 1]
            cl = segs[i - 1][2]
            cr = segs[i + 1][2]
            if cl - (segs[i - 1][0] >= l) > 0 \
                    and cr - (segs[i - 1][0] <= r) > 0:
                c[e] += 1
            if cl == 0 and cr == 0:
                c[e] -= 1
        if cd > 0 and p == False:
            res += 1
        p = (cd > 0)
    z = c[0]
    for i in range(0, 2 * n, 2):
        z = max(z, c[i])
    print(res + z)


for i in range(mint()):
    solve()
