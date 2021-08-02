from copy import deepcopy
from collections import deque
from sys import stdin
nii = lambda: map(int, stdin.readline().split())
lnii = lambda: list(map(int, stdin.readline().split()))

n, m = nii()
l = [lnii() for i in range(m)]


def BFS(t_l):
    tree = [[] for i in range(n)]
    for a, b in t_l:
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)

    dist = [-1 for i in range(n)]
    dist[0] = 0

    que = deque()
    que.append(0)

    while que:
        x = que.popleft()
        for i in tree[x]:
            if dist[i] == -1:
                que.append(i)
                dist[i] = dist[x] + 1

    return dist


ans = 0
for i in range(m):
    t_l = deepcopy(l)
    del t_l[i]
    dist = BFS(t_l)
    if -1 in dist:
        ans += 1

print(ans)
