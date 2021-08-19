import heapq
import sys


class FTree:

    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & -s

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, j - 1)
        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    def select(self, k):
        lo = 1
        hi = self.n
        for i in range(30):
            mid = (lo + hi) // 2
            if self.query(1, mid) < k:
                lo = mid
            else:
                hi = mid
        return hi


class RUPQ:

    def __init__(self, n):
        self.ftree = FTree([0] * n)

    def query(self, i):
        return self.ftree.query(1, i)

    def update(self, i, j, v):
        self.ftree.update(i, v)
        self.ftree.update(j + 1, -v)


class RURQ:

    def __init__(self, n):
        self.f = FTree([0] * n)
        self.r = RUPQ(n)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        return self.r.query(j) * j - self.f.query(1, j)

    def update(self, i, j, v):
        self.r.update(i, j, v)
        self.f.update(i, v * (i - 1))
        self.f.update(j + 1, -1 * v * j)


(n, k) = [int(i) for i in sys.stdin.readline().split()]
mmn = 1
mmx = 200000
ftree = RUPQ(mmx)
lns = sys.stdin.readlines()
bds = []
qqq = 0
for ln in lns:
    qqq += 1
    t = [int(i) for i in ln.split()]
    t.append(qqq)
    bds.append(t)
    ftree.update(bds[-1][0], bds[-1][1], 1)
bds.sort()
bind = 0
heap = []
ans = []
for i in range(1, mmx + 1):
    while bind < n and bds[bind][0] == i:
        heapq.heappush(heap, (-1 * bds[bind][1], bds[bind][2]))
        bind += 1
    while ftree.query(i) > k:
        (bd, bnd) = heapq.heappop(heap)
        ans.append(bnd)
        ftree.update(i, -1 * bd, -1)
print(len(ans))
print(*ans)
