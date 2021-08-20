import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def check(s, n, v):
    for i in range(n):
        if s[i:i + n].count(v) == 0:
            return False
    return True


def solve():
    (p, f) = mints()
    (cs, cw) = mints()
    (s, w) = mints()
    best = 0
    for i in range(cs + 1):
        if i * s > p:
            break
        h = p - i * s
        j = min(h // w, cw)
        hs = cs - i
        hw = cw - j
        if s < w:
            a = min(f // s, hs)
            b = min((f - a * s) // w, hw)
        else:
            a = min(f // w, hw)
            b = min((f - a * w) // s, hs)
        best = max(best, i + j + a + b)
    print(best)


for i in range(mint()):
    solve()
