import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n, T, a, b = mints()
    h = list(mints())
    c = [0, 0]
    for i in h:
        c[i] += 1
    i = 0
    t = [None] * n
    for j in mints():
        t[i] = (j, i)
        i += 1
    t.sort()
    tt = 0
    tmust = 0
    cmust = 0
    r = 0
    for ii in range(len(t)):
        tn, i = t[ii]
        if tt < tn - 1:
            tt = tn - 1
            left = tt - tmust
            if left >= 0:
                ac = min(left // a, c[0])
                bc = min((left - ac * a) // b, c[1])
                #print(tt, tmust, left, cmust, ac, bc)
                r = max(r, cmust + ac + bc)
        if h[i]:
            tmust += b
            c[1] -= 1
        else:
            tmust += a
            c[0] -= 1
        #print("tmust", tmust)
        cmust += 1
    if tt < T:
        tt = T
        left = tt - tmust
        if left >= 0:
            ac = min(left // a, c[0])
            bc = min((left - ac * a) // b, c[1])
            r = max(r, cmust + ac + bc)
    return r


for i in range(mint()):
    print(solve())
