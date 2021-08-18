import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)


def ni(): return int(ns())
def nin(y): return [ni() for _ in range(y)]
def na(): return list(map(int, stdin.readline().split()))
def nan(y): return [na() for _ in range(y)]
def nf(): return float(ns())
def nfn(y): return [nf() for _ in range(y)]
def nfa(): return list(map(float, stdin.readline().split()))
def nfan(y): return [nfa() for _ in range(y)]
def ns(): return stdin.readline().rstrip()
def nsn(y): return [ns() for _ in range(y)]
def ncl(y): return [list(ns()) for _ in range(y)]
def nas(): return stdin.readline().split()


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
