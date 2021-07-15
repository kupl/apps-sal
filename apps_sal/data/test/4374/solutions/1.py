import sys


def dfs(v, d, prev, i):
    nonlocal mid
    nonlocal M
    M[v] = False
    way[d] = v
    if way[d + 1] == 0:
        mid[i] = way[d // 2]
    mx = (d, v)
    for x in E[v]:
        if x != prev:
            mx = max(mx, dfs(x, d + 1, v, i))

    return mx


sys.setrecursionlimit(2000)
n, m = list(map(int, input().split()))

E = [[] for i in range(n + 1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    E[a].append(b)
    E[b].append(a)

mid = [0] * (n + 2)
c = 0
k = 0
way = [0] * (n + 2)

M = [True] * (n + 1)
M[0] = False
i = -1
while True in M:
    i += 1
    idx = M.index(True)
    p1 = dfs(idx, 0, 0, i)[1]
    way = [0] * (n + 2)
    s, p2 = dfs(p1, 0, 0, i)
    if s > c:
        c = s
        k = i
r = []
for j in range(0, i + 1):
    if j == k:
        continue
    r.append((mid[k], mid[j]))
    E[mid[k]].append(mid[j])
    E[mid[j]].append(mid[k])
p1 = dfs(1, 0, 0, n + 1)[1]
s, p2 = dfs(p1, 0, 0, n + 1)
print(s)
for item in r:
    print(item[0], item[1])

