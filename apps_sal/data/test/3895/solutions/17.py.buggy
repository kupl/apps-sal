n = int(input())
f = list(map(int, input().split()))
h = []
ind_h = [-1] * (n + 1)
g = [0] * n
occs = {}
for i in range(len(f)):
    if f[i] not in occs:
        occs[f[i]] = {i + 1}
        h.append(f[i])
        ind_h[f[i]] = len(h) - 1
        g[i] = len(h)
    else:
        g[i] = ind_h[f[i]] + 1
        occs[f[i]].add(i + 1)
for k in occs:
    if k not in occs[k]:
        print(-1)
        return
print(len(h))
print(*g)
print(*h)
