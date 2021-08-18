
import sys


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


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 10 ** 9 + 7


class SegTreeIndex:

    def __init__(self, n, func, init):

        self.n = n
        self.func = func
        self.init = init
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [self.init] * (n2 << 1)
        self.index = [self.init] * (n2 << 1)
        for i in range(n2):
            self.index[i + n2] = i
        for i in range(n2 - 1, -1, -1):
            self.index[i] = self.index[i * 2]

    def update(self, i, x):

        i += self.n2
        self.tree[i] = x
        while i > 1:
            left, right = min(i, i ^ 1), max(i, i ^ 1)
            if self.func(self.tree[left], self.tree[right]) == self.tree[left]:
                self.tree[i >> 1] = self.tree[left]
                self.index[i >> 1] = self.index[left]
            else:
                self.tree[i >> 1] = self.tree[right]
                self.index[i >> 1] = self.index[right]
            i >>= 1

    def query(self, a, b):

        l = a + self.n2
        r = b + self.n2
        s = (self.init, -1)
        while l < r:
            if r & 1:
                r -= 1
                res = self.func(s[0], self.tree[r])
                if res == s[0]:
                    pass
                else:
                    s = (self.tree[r], self.index[r])
            if l & 1:
                res = self.func(self.tree[l], s[0])
                if res == self.tree[l]:
                    s = (self.tree[l], self.index[l])
                else:
                    pass
                l += 1
            l >>= 1
            r >>= 1
        return s


N, K = MAP()
MAX = 200007

LRs = [[] for i in range(MAX + 2)]
R = [0] * (N + 1)
for i in range(N):
    l, r = MAP()
    LRs[l].append(i + 1)
    LRs[r + 1].append(-(i + 1))
    R[i + 1] = r

sti = SegTreeIndex(N + 1, max, -INF)
segcnt = 0
ans = []
removed = set()
for i in range(1, MAX + 2):
    for idx in LRs[i]:
        if idx > 0:
            sti.update(idx, R[idx])
            segcnt += 1
        else:
            idx = abs(idx)
            if idx not in removed:
                sti.update(idx, -INF)
                segcnt -= 1
    while segcnt > K:
        mx, idx = sti.query(0, N + 1)
        sti.update(idx, -INF)
        ans.append(idx)
        removed.add(idx)
        segcnt -= 1
print(len(ans))
print(*ans)
