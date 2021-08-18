import sys
n, m = list(map(int, input().split()))

sys.setrecursionlimit(10**9)

root = [-1 for i in range(n + 1)]
dep = [1] * (n + 1)


def r(x):
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]


def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    if dep[x] == dep[y]:
        dep[x] += 1
    if dep[x] < dep[y]:
        x, y = y, x
    root[x] += root[y]
    root[y] = x


for i in range(m):
    x, y, z = list(map(int, input().split()))
    unite(x, y)


g = [0] * (n + 1)
for i in range(1, n + 1):
    g[r(i)] += 1
ans = 0
for i in range(n + 1):
    if g[i] > 0:
        ans += 1
print(ans)
