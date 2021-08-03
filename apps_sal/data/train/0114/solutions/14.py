import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n = int(I())
    a = list(map(int, I().split()))
    m = int(I())
    pl = sorted([list(map(int, I().split())) for _ in range(m)])
    pln, mxs = [], 0
    for x in pl[::-1]:
        if x[1] > mxs:
            pln.append(x)
        mxs = max(mxs, x[1])
    pl = pln[::-1]
    m = len(pl)
    p, s = list(map(list, list(zip(*pl))))
    if max(a) > max(p):
        print(-1)
    else:
        days = 0
        c = 0
        d2 = 1
        while d2 <= m:
            d2 *= 2
        d2 //= 2
        while c < n:
            days += 1
            mx = 0
            inday = 0
            while c < n:
                mx = max(mx, a[c])
                inday += 1
                pi = -1
                d = d2
                while d:
                    np = pi + d
                    if np < m and p[np] < mx:
                        pi = np
                    d //= 2
                pi += 1
                if pi < m and s[pi] >= inday:
                    c += 1
                else:
                    break
        print(days)
