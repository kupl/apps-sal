import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n, m = mints()
    q = list(mints())
    w = dict()
    for i in q:
        w[i] = 0
    ql = 0
    c = 0
    ss = 0
    y = []
    while ql < len(q):
        p = q[ql]
        ql += 1
        x = p - 1
        if x not in w:
            d = w[p] + 1
            y.append(x)
            q.append(x)
            ss += d
            w[x] = d
            c += 1
            if c == m:
                break
        x = p + 1
        if x not in w:
            d = w[p] + 1
            q.append(x)
            y.append(x)
            ss += d
            w[x] = d
            c += 1
            if c == m:
                break
    print(ss)
    print(' '.join(map(str, y)))


solve()
