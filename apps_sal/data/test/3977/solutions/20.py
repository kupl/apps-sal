def dfs(u, vis):
    vis.add(u)
    for v in g[u]:
        if v not in vis:
            dfs(v, vis)


(n, m, k) = list(map(int, list(input().split())))
govs_ind = list(map(int, list(input().split())))
orig = set()
countries = set(range(1, n + 1))
g = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = list(map(int, list(input().split())))
    if u > v:
        (u, v) = (v, u)
    orig.add((u, v))
    g[u].append(v)
    g[v].append(u)
gov_nods = []
for u in govs_ind:
    vis = set()
    dfs(u, vis)
    gov_nods.append(vis)
no_govs = countries.copy()
nvoss = 0
for reg in gov_nods:
    no_govs -= reg
    size = len(reg)
    nvoss += size * (size - 1) // 2
size = len(no_govs)
nvoss += size * (size - 1) // 2
maxi = 0
for i in range(len(gov_nods)):
    if len(gov_nods[i]) > len(gov_nods[maxi]):
        maxi = i
max_gov = gov_nods[maxi]
nvoss += len(max_gov) * len(no_govs)
nvoss -= len(orig)
print(nvoss)
