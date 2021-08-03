from itertools import tee
from sys import setrecursionlimit
from sys import stdin
setrecursionlimit(1000000007)
_data = iter(stdin.read().split('\n'))


def input():
    return next(_data)


class SegTree:
    def __init__(self, n, zero, f):
        while n & (n - 1):
            n -= n & -n
        self.n = 2 * n
        self.zero = zero
        self.f = f
        self.t = [self.zero for _ in range(2 * self.n - 1)]

    def __getitem__(self, k):
        return self.t[k + self.n - 1]

    def __setitem__(self, k, v):
        k += self.n - 1
        self.t[k] = v
        while k > 0:
            k = (k - 1) >> 1
            self.t[k] = self.f(self.t[2 * k + 1], self.t[2 * k + 2])

    def query(self, a, b):
        ans = self.zero
        t1 = [0]
        t2 = [0]
        t3 = [self.n]
        while t1:
            k, l, r = t1.pop(), t2.pop(), t3.pop()
            if b <= l or r <= a:
                continue
            elif a <= l and r <= b:
                ans = self.f(self.t[k], ans)
            else:
                t1.append(2 * k + 1), t2.append(l), t3.append((l + r) >> 1)
                t1.append(2 * k + 2), t2.append((l + r) >> 1), t3.append(r)
        return ans


n, m, k = [int(x) for x in input().split()]
st = tuple(SegTree(n, 0, max) for _ in range(m))
rv = -1
rt = (0,) * m
p = 0
t = [0] * m
for i in range(n):
    a = tuple(int(x) for x in input().split())
    for j in range(m):
        st[j][i] = a[j]
        t[j] = max(t[j], a[j])
    while sum(t) > k:
        p += 1
        for j in range(m):
            t[j] = st[j].query(p, i + 1)
    if rv < (i + 1) - p:
        rv = (i + 1) - p
        rt = tuple(t)
print(*rt)
