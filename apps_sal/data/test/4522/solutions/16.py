from operator import itemgetter
import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.cnt -= 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return -self.parent[self.root(x)]

    def get_cnt(self):
        return self.cnt


n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n - 1)]
q = list(map(int, input().split()))
info = sorted(info, key = itemgetter(2))
ans = [0] * (2*10**5)
uf = UnionFind(2*10**5)
info_i = 0
for i in range(2*10**5):
    if i-1 >= 0:
        ans[i] = ans[i-1]
    while True:
        if info_i >= n - 1:
           break
        if info[info_i][2] == i + 1:
            a, b, _ = info[info_i]
            a -= 1
            b -= 1
            num_a = uf.get_size(a)
            num_b = uf.get_size(b)
            num_ab = num_a + num_b
            comb_num_a = (num_a*(num_a-1)) // 2
            comb_num_b = (num_b*(num_b-1)) // 2
            comb_num_ab = (num_ab*(num_ab-1)) // 2
            ans[i] += comb_num_ab - (comb_num_a + comb_num_b)
            uf.merge(a, b)
            info_i += 1
        else:
            break

res = [0] * len(q)
for i, j in enumerate(q):
    res[i] = ans[j - 1]
print(*res)
