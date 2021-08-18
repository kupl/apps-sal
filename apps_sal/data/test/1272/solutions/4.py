import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
sys.setrecursionlimit(200000)
b = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(M)]


class uf:
    def __init__(self, n):
        self.n = n
        self.l = [-1] * n

    def ro(self, n):
        if self.l[n] < 0:
            return n
        r = self.ro(self.l[n])
        self.l[n] = r
        return r

    def me(self, a, b):
        ra = self.ro(a)
        rb = self.ro(b)
        if self.l[ra] > self.l[rb]:
            ra, rb = rb, ra
        if ra != rb:
            self.l[ra] += self.l[rb]
            self.l[rb] = ra

    def size(self, n):
        return -self.l[self.ro(n)]

    def sa(self, a, b):
        return self.ro(a) == self.ro(b)

    def rl(self):
        return [i for i, v in enumerate(self.l) if v < 0]

    def len(self):
        return len(self.rl())

    def ul(self):
        d = {n: i for i, n in enumerate(self.rl())}
        m = [[]for i in range(self.len())]
        for i in range(self.n):
            m[d[self.ro(i)]].append(i)
        return m

    def __str__(self):
        return f"{self.ul()}"


l = [0] * M
s = uf(N)
h = N * (N - 1) // 2
for i in range(M - 1, -1, -1):
    l[i] = h
    if s.ro(b[i][0]) != s.ro(b[i][1]):
        h -= s.size(b[i][0]) * s.size(b[i][1])
        s.me(b[i][0], b[i][1])
print(*l, sep="\n")
