from math import factorial as f


class DSU:
    def __init__(self, N):
        # stores parent node of given vertex
        self.parents = list(range(N))
        # gives size of component w given node
        self.size = [1] * N

    # runtime: amoritized O(1)
    # returns root node
    def find(self, x):
        root = x
        # finds parent node at the end of the chain
        while self.parents[root] != root:
            root = self.parents[root]

        # optional: path compression
        while (x != root):
            nextx = self.parents[x]
            self.parents[x] = root
            x = nextx

        return root

    # runtime: amortized O(1) by combining union by size and path compression
    # unifies two components together (the ones containing x and y)
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        # if they're in same group, do nothing
        if xr == yr:
            return False

        if self.size[xr] > self.size[yr]:
            xr, yr = yr, xr
        # size of xr >= size of yr
        # smaller points to the larger
        self.parents[xr] = yr
        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        return True

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def getSize(self, x):
        return self.size[self.find(x)]


# from collections import defaultdict, Counter, deque
# from heapq import heappop, heappush, heapify
# from functools import lru_cache, reduce
# import bisect
# from itertools import permutations, combinations, combinations_with_replacement

mod = 998244353
n, K = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# num of pairs you can swap
row_dsu = DSU(n)
col_dsu = DSU(n)

# find rows
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
