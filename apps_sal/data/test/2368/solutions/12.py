import sys
from collections import defaultdict


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n  # 各要素の親 親自身は -i (i は集合の要素数)

    def r(self, x):  # x の 親を返す
        if self.root[x] < 0:  # 自身が親
            return x
        else:  # 再帰的に親を辿る
            self.root[x] = self.r(self.root[x])
            return self.root[x]

    def union(self, x, y):  # x と y を連結
        x = self.r(x)
        y = self.r(y)
        if x == y:
            return  # 親が同じなら何もしない
        self.root[x] += self.root[y]
        self.root[y] = x

    def find(self, x, y) -> bool:  # x と y は同じ集合に属しているか
        return self.root[x] == self.root[y]

    # オプション
    def size(self, x) -> int:  # x が属する集合の要素数
        x = self.r(x)
        return -self.root[x]

    def members(self, x):
        '''要素 x が属する集合の要素をリストを返す'''
        root = self.r(x)
        return [i for i in range(self.n) if self.r(i) == root]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.r(member)].append(member)
        return group_members


n, m = LI()
a = LI()
b = LI()
uf = UnionFind(n)
for _ in range(m):
    c, d = LI()
    c -= 1
    d -= 1
    uf.union(c, d)


is_ok = True
mems = list(uf.all_group_members().values())

for mem in mems:
    a_sum = 0
    b_sum = 0
    for j in mem:
        a_sum += a[j]
        b_sum += b[j]
    if a_sum != b_sum:
        is_ok = False
        break

print(("Yes" if is_ok else "No"))

