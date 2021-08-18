from collections import Counter
import math
import statistics
import itertools
N, M = list(map(int, input().split()))
par = [i for i in range(1, N + 1)]
rank = [0] * N


def find(x):
    if par[x - 1] == x:
        return x
    else:
        par[x - 1] = find(par[x - 1])
        return par[x - 1]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x - 1] < rank[y - 1]:
        par[x - 1] = y
    else:
        par[y - 1] = x
        if rank[x - 1] == rank[y - 1]:
            rank[x - 1] += 1


for i in range(M):
    a, b = list(map(int, input().split()))
    unite(a, b)

cnt = [0] * N
for i in range(N):
    cnt[find(i) - 1] += 1
print((max(cnt)))
