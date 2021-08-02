from collections import defaultdict


n = int(input())
g = defaultdict(list)
cs = [None] * n

for v, _ in enumerate(range(n)):
    p, c = map(int, input().split())
    if p != -1:
        g[p - 1].append(v)
    cs[v] = c

r = []
used = [False] * n


def dfs(g, stack):
    nonlocal r, used
    while stack:
        v = stack.pop()
        used[v] = True

        flag = True if cs[v] == 1 else False
        for u in g[v]:
            if not used[u]:
                stack.append(u)
            if cs[u] == 0:
                flag = False

        if flag:
            r.append(v)


for v in range(n):
    if not used[v]:
        dfs(g, [v])

if r:
    for el in sorted(r):
        print(el + 1, end=" ")
else:
    print(-1)
