import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.sizes = [1] * (n + 1)

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        d1 = self.par[x]
        d2 = self.par[y]
        if d1 <= d2:
            self.par[y] = x
            self.sizes[x] = self.sizes[x] + self.sizes[y]
            if d1 == d2:
                self.par[x] = self.par[x] - 1
        else:
            self.par[x] = y
            self.sizes[y] = self.sizes[x] + self.sizes[y]

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # サイズ
    def size(self, x):
        return self.sizes[self.find(x)]

    # 木の数
    def number(self):
        count = 0
        for i in self.par[1:]:
            if i < 0:
                count = count + 1
        return count


U = UnionFind(n)
for i in range(m):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    U.union(c, d)
# print(U)
check = {}
for i in range(n):
    x = U.find(i)
    if x in check:
        check[x].append(i)
    else:
        check[x] = [i]

for i in check:
    l = check[i]
    A = 0
    B = 0
    for j in l:
        A += a[j]
        B += b[j]
    if A != B:
        print('No')
        return
print('Yes')
