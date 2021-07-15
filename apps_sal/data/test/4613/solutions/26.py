from collections import Counter
N, M = map(int, input().split())

class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy


A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

count = 0
for i in range(M):
    uni = UnionFind(N)
    for j in range(M):
        if j == i:
            continue
        uni.merge(A[j], B[j])
    # UnionFindの連結成分の個数を数える
    roots = [uni[x] for x in uni.root[1:]]
    counter = Counter(roots)
    if len(counter) > 1:
        count += 1

print(count)
