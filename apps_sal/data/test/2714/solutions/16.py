from collections import deque
import sys
input = sys.stdin.readline


class Unionfind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        p = x

        while not self.par[p] < 0:
            p = self.par[p]

        while x != p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p

        return p

    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.par[rx] += self.par[ry]
        self.par[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


def bfs(s):
    q = deque([s])
    color[s] = 1
    b, w = 1, 0

    while q:
        v = q.popleft()

        for nv in adj_list[v]:
            if color[nv] == 0:
                color[nv] = -color[v]
                q.append(nv)

                if color[nv] == 1:
                    b += 1
                else:
                    w += 1
            else:
                if color[nv] == color[v]:
                    return -1, -1

    return b, w


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    uf = Unionfind(n)
    MOD = 998244353

    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)
        uf.unite(u - 1, v - 1)

    roots = set(uf.root(i) for i in range(n))
    ans = 1
    color = [0] * n

    for r in roots:
        if uf.count(r) == 1:
            ans *= 3
        else:
            b, w = bfs(r)

            if b == -1:
                ans = 0
                break
            else:
                ans *= pow(2, b, MOD) + pow(2, w, MOD)

        ans %= MOD

    print(ans)
