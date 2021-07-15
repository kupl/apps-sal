import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

n, m = na()

if m == 1:
    print(1, 2)
    return

if m % 2 == 0:
    l = (m + 1) // 2
    r = (m + 1) // 2 + 2
    cnt = 0
    while cnt < m and l >= 1 and r <= (m + 1):
        print(l, r)
        l -= 1
        r += 1
        cnt += 1
    l = (n - m - 1) // 2
    r = (n - m - 1) // 2 + 1
    while cnt < m and l >= 1 and r <= (n - m - 1):
        print(m + 1 + l, m + 1 + r)
        l -= 1
        r += 1
        cnt += 1
else:
    l = m // 2
    r = m // 2 + 2
    cnt = 0
    while cnt < m and l >= 1 and r <= m:
        print(l, r)
        l -= 1
        r += 1
        cnt += 1
    l = (n - m) // 2
    r = (n - m) // 2 + 1
    while cnt < m and l >= 1 and r <= (n - m):
        print(m + l, m + r)
        l -= 1
        r += 1
        cnt += 1
