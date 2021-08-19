from copy import deepcopy
(n, k, m, a) = [int(i) for i in input().split()]
cn = [0] * (n + 1)
last = [-1] * (n + 1)
v = [int(i) for i in input().split()]
for i in range(len(v)):
    last[v[i]] = i
    cn[v[i]] += 1
cn1 = deepcopy(cn)
last1 = deepcopy(last)
for i in range(1, n + 1):
    cn = deepcopy(cn1)
    last = deepcopy(last1)
    res = [i1 for i1 in range(1, n + 1)]
    res.sort(key=lambda x: (cn[x], -last[x]), reverse=True)
    for j in range(len(res)):
        if res[j] != i:
            continue
        j1 = j + 1
        lft = m - a
        while j1 < n and lft:
            pls = min(lft, cn[i] - cn[res[j1]] + 1)
            cn[res[j1]] += min(lft, cn[i] - cn[res[j1]] + 1)
            last[res[j1]] = m
            lft -= pls
            j1 += 1
    res.sort(key=lambda x: (cn[x], -last[x]), reverse=True)
    sans = 0
    for j in range(len(res)):
        if res[j] != i:
            continue
        if cn[i] == 0 or j >= k:
            sans = 0
        else:
            sans = 1
        break
    if sans == 1:
        print(1, end=' ')
        continue
    cn = deepcopy(cn1)
    last = deepcopy(last1)
    if m - a:
        cn[i] += m - a
        last[i] = m - 1
    res.sort(key=lambda x: (cn[x], 0 - last[x]), reverse=True)
    for j in range(len(res)):
        if res[j] != i:
            continue
        if cn[i] == 0 or j >= k:
            sans = 0
        else:
            sans = 1
        break
    if sans:
        print(2, end=' ')
    else:
        print(3, end=' ')
