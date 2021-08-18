#from collections import deque,defaultdict
import bisect
import itertools
def printn(x): return print(x, end='')
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True  # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353


def ddprint(x):
    if DBG:
        print(x)


n, m = inm()
w = inl()
vl = []
vs = []
for i in range(m):
    l, v = inm()
    vl.append((v, l))
    vs.append(v)
if max(w) > min(vs):
    print(-1)
    return
w.sort()

vl.sort()
b = []
mx = -1
for i in range(m):
    mx = max(mx, vl[i][1])
    if len(b) > 0 and b[-1][0] == vl[i][0]:
        b.pop()
    b.append((vl[i][0], mx))

pms = itertools.permutations(w[:-2], n - 2)
mn = BIG
for pm in pms:
    pml = list(pm)
    pml.append(w[n - 2])
    a = [0]
    ww = [w[n - 1]]
    for i in range(n - 1):
        x = a[-1]
        u = pml[i]
        for k in range(i, -1, -1):
            u += ww[k]
            p = bisect.bisect_left(b, (u, -1))
            if p > 0 and b[p - 1][1] > x - a[k]:
                #ddprint(f"add l {j=} {k=} {l=} {u=} {v=}")
                x = a[k] + b[p - 1][1]
        a.append(x)
        ww.append(pml[i])
    # ddprint(pml)
    # ddprint(a)
    mn = min(mn, a[-1])
print(mn)
