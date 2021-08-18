from collections import Counter
from random import random
import sys
sys.setrecursionlimit(500000)


def scc(N, G, RG):
    # https://tjkendev.github.io/procon-library/python/graph/scc.html
    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


N, M = list(map(int, input().split()))
E = [[] for _ in range(N + 1)]
E_set = [set() for _ in range(N + 1)]
E_rev = [[] for _ in range(N + 1)]
E_rev_set = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    E[a].append(b)
    E_set[a].add(b)
    E_rev[b].append(a)
    E_rev_set[b].add(a)

label, group = scc(N + 1, E, E_rev)
cnt = Counter(group)
Closed = [False] * (N + 1)

grooo = [set() for _ in range(N + 1)]
for v, gr in enumerate(group):
    grooo[gr].add(v)

haaaaaaaaaaaaaaaaaaaaaaa = enumerate(group) if random() > 0.5 else list(zip(list(range(N, 0, -1)), group[::-1]))


for v, gr in haaaaaaaaaaaaaaaaaaaaaaa:
    if Closed[gr]:
        continue
    Closed[gr] = True
    if cnt[gr] == 1:
        continue

    #print(gr, cnt[gr])
    groo = grooo[gr]

    path = [v]
    path_set = {v}
    while True:
        # print("v=",v)
        aaa = E_set[v] & path_set
        if aaa:
            break
        u = (groo & E_set[v]).pop()
        # print("u=",u)
        while E_rev_set[u] - {v} & path_set:
            path_set.remove(path.pop())
        path.append(u)
        path_set.add(u)
        v = u
        # print(path)
    for i, v in enumerate(path):
        if v in aaa:
            aaa.remove(v)
            if len(aaa) == 0:
                break
    ans = path[i:]
    print((len(ans)))
    print(("\n".join(map(str, ans))))
    return
print((-1))
