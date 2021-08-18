
import sys
from bisect import bisect_left


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7


class SegTree:

    def __init__(self, n, func, intv, A=[]):

        self.n = n
        self.func = func
        self.intv = intv
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [self.intv] * (n2 << 1)
        if A:
            for i in range(n):
                self.tree[n2 + i] = A[i]
            for i in range(n2 - 1, -1, -1):
                self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i, x):

        i += self.n2
        self.tree[i] = x
        while i > 0:
            i >>= 1
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, a, b):

        l = a + self.n2
        r = b + self.n2
        s = self.intv
        while l < r:
            if r & 1:
                r -= 1
                s = self.func(s, self.tree[r])
            if l & 1:
                s = self.func(s, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return s

    def get(self, i):
        return self.tree[i + self.n2]

    def all(self):
        return self.tree[1]


def bisearch_max(mn, mx, func):

    ok = mn
    ng = mx
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


def check(m):
    mx = st.query(cur, m)
    idx = bisect_left(P, mx)
    if idx == M:
        return False
    _, s = PS[idx]
    scnt = m - cur
    return s >= scnt


ans = []
for _ in range(INT()):
    N = INT()
    A = LIST()
    M = INT()
    PS = []
    for i in range(M):
        p, s = MAP()
        PS.append((p, s))

    PS.sort()
    for i in range(M - 1, 0, -1):
        if PS[i][1] > PS[i - 1][1]:
            PS[i - 1] = (PS[i - 1][0], PS[i][1])
    P, _ = list(zip(*PS))

    st = SegTree(N, max, 0, A)
    cur = day = 0
    while cur < N:
        res = bisearch_max(cur, N + 1, check)
        if res == cur:
            ans.append(str(-1))
            break
        cur = res
        day += 1
    else:
        ans.append(str(day))

print('\n'.join(ans))
