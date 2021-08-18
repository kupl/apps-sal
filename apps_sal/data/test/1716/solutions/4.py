from itertools import accumulate
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


N, M, Q = mi()
bit = BIT(N)
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
        bit.add(lrpq[i][1] + 1, 1)
    else:
        bit.sum(lrpq[i][2])
        if lrpq[i][1] > 0:
            ans[lrpq[i][0] - M] = bit.sum(lrpq[i][2] + 1) - bit.sum(lrpq[i][1])
        else:
            ans[lrpq[i][0] - M] = bit.sum(lrpq[i][2] + 1)

for num in ans:
    print(num)
