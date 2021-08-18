import sys

sys.setrecursionlimit(10**6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


class BIT:
    def __init__(self, n):
        self.inf = 10**9
        self.n = n + 3
        self.table = [self.inf] * (self.n + 1)

    def update(self, i, x):
        i += 1
        while i <= self.n:
            if x < self.table[i]:
                self.table[i] = x
            i += i & -i

    def min(self, i):
        i += 1
        res = self.inf
        while i > 0:
            if self.table[i] < res:
                res = self.table[i]
            i -= i & -i
        return res


inf = 10**9
n, q = MI()
ans = (n - 2)**2
t = l = n
yo = []
ta = []
for i in range(q):
    op, x = MI()
    if op == 1:
        ta.append((i, x))
    else:
        yo.append((i, x))

if not ta or not yo:
    ans -= (len(ta) + len(yo)) * (n - 2)
    print(ans)
    return


def cnt(ia, jb):
    res = 0
    bit = BIT(q + 5)
    for i, a in ia:
        bit.update(i, a)
    jb.sort(key=lambda x: x[1])
    now = 2
    for j, b in jb:
        cur = bit.min(j)
        if cur == inf:
            cur = n
        # print(j,b,cur)
        now = max(now, cur)
        res += now - 2
    return res


ans -= cnt(ta, yo)
ans -= cnt(yo, ta)
print(ans)
