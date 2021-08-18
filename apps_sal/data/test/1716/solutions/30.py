from itertools import accumulate
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


def segfunc(a, b):
    return a + b


def init(init_val):
    for i in range(n):
        seg[i + num - 1] = init_val[i]
    for i in range(num - 2, -1, -1):
        seg[i] = segfunc(seg[2 * i + 1], seg[2 * i + 2])


def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = segfunc(seg[k * 2 + 1], seg[k * 2 + 2])


def query(p, q):
    if q <= p:
        return ide_ele
    p += num - 1
    q += num - 2
    res = ide_ele
    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res


n, M, Q = mi()

ide_ele = 0
num = 2**(n - 1).bit_length()
seg = [ide_ele] * 2 * num

L = [0] * n
init(L)

lrpq = dp2(0, 3, M + Q)

for i in range(M):
    l, r = mi()
    lrpq[i][1] = l - 1
    lrpq[i][2] = r - 1

for i in range(M, M + Q):
    p, q = mi()
    lrpq[i][0] = i
    lrpq[i][1] = p - 1
    lrpq[i][2] = q - 1

lrpq = sorted(lrpq, key=lambda x: (x[2], x[0]))

ans = [0] * (Q)

for i in range(M + Q):
    if lrpq[i][0] == 0:
        update(lrpq[i][1], seg[lrpq[i][1] + num - 1] + 1)
    else:
        ans[lrpq[i][0] - M] = query(lrpq[i][1], lrpq[i][2] + 1)

for num in ans:
    print(num)
