import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    f = list(mints())
    w = [False] * (n + 1)
    p = [False] * (n + 1)
    for i in f:
        p[i] = True
    q = []
    for i in range(1, n + 1):
        if w[i] or p[i]:
            continue
        s = i
        e = i
        w[i] = True
        ok = True
        while f[e - 1] != 0:
            e = f[e - 1]
            if e == s:
                ok = False
                break
            w[e] = True
        if ok:
            q.append((s, e))
    for i in range(len(q) - 1):
        f[q[i][1] - 1] = q[i + 1][0]
    f[q[-1][1] - 1] = q[0][0]
    print(' '.join(map(str, f)))


solve()
