"""

created by shuangquan.huang at 12/14/18

"""
import collections
import sys
N = int(input())
p = [int(x) for x in input().split()]
G = collections.defaultdict(list)
for (i, v) in enumerate(p):
    u = i + 2
    G[u].append(v)
    G[v].append(u)
root = 1
colors = [0] * (N + 1)
counts = [0] * (N + 1)
q = [root]
parents = [0] * (N + 1)
vis = [0] * (N + 1)
while q:
    u = q.pop()
    if vis[u]:
        colors[parents[u]] += colors[u]
        continue
    children = [v for v in G[u] if v != parents[u]]
    for v in children:
        parents[v] = u
    if children:
        vis[u] = True
        q.append(u)
        q.extend(children)
    else:
        vis[u] = True
        colors[u] = 1
        colors[parents[u]] += 1
colors = colors[1:]
colors.sort()
print(' '.join(map(str, colors)))
