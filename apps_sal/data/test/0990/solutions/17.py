from collections import defaultdict


def dfs(s, t, links):
    visited = set()
    q = [(s, 0)]
    while q:
        v, used = q.pop()
        if v == t:
            return used
        visited.add(v)
        for lb, u in links[v]:
            if u in visited:
                continue
            q.append((u, used | lb))


n = int(input())
links = [set() for _ in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    lb = 1 << i
    links[a].add((lb, b))
    links[b].add((lb, a))
conditions = []
m = int(input())
for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    conditions.append(dfs(u, v, links))

link_conditions = [int(''.join(b), 2) for b in zip(*list(map(('{:0' + str(n - 1) + 'b}').format, conditions)))]

dp = defaultdict(lambda: 0)
dp[0] = 1
for lc in link_conditions:
    for fulfilled, pattern in list(dp.items()):
        dp[fulfilled | lc] += pattern
print((dp[(1 << m) - 1]))
