import sys
def input(): return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM(): return map(int, input().split())
def L(): return list(NM())
def LN(n): return [N() for i in range(n)]
def LL(n): return [L() for i in range(n)]


t = N()


def f():
    n, x, m = NM()
    lo = x
    hi = x
    for i in range(m):
        l, r = NM()
        if l <= lo <= r:
            lo = l
        if l <= hi <= r:
            hi = r
    print(hi - lo + 1)


for i in range(t):
    f()
