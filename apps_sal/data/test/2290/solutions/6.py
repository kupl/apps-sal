from sys import stdin

input = stdin.readline

edge = [[] for _ in range(200005)]
n, m = map(int, input().split())

check = [0] * 200005
mx = 0

from collections import deque

def dfs(x):
    l = deque([x])
    check[x] = 1
    while len(l):
        p = l.popleft()
        nonlocal mx
        mx = max(mx,p)
        for i in edge[p]:
            if check[i]:
                continue
            l.append(i)
            check[i] = 1


for i in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

r = 0
ans = 0
for i in range(1, n + 1):
    if check[i]:
        continue
    mx = 0
    dfs(i)
    if i <= r:
        ans += 1
    r = max(r, mx)

print(ans)
