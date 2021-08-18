from math import factorial as f


class DSU:
    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [1] * N

    def find(self, x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]

        while (x != root):
            nextx = self.parents[x]
            self.parents[x] = root
            x = nextx

        return root

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False

        if self.size[xr] > self.size[yr]:
            xr, yr = yr, xr
        self.parents[xr] = yr
        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        return True

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def getSize(self, x):
        return self.size[self.find(x)]


mod = 998244353
n, K = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

row_dsu = DSU(n)
col_dsu = DSU(n)

for i in range(n):
    for j in range(i):
        if all(arr[i][k] + arr[j][k] <= K for k in range(n)):
            row_dsu.union(i, j)
        if all(arr[k][i] + arr[k][j] <= K for k in range(n)):
            col_dsu.union(i, j)

row_set = set()
col_set = set()
for i in range(n):
    row_set.add(row_dsu.find(i))
    col_set.add(col_dsu.find(i))

row_prod = col_prod = 1
for ele in row_set:
    row_prod *= f(row_dsu.size[ele])
for ele in col_set:
    col_prod *= f(col_dsu.size[ele])

print(((row_prod * col_prod) % mod))
