from collections import Counter
(n, k) = list(map(int, input().split()))
a = [tuple(map(int, input().split())) for _ in range(n)]
f = [1, 1]
mod = 998244353
for i in range(2, n + 7):
    f.append(f[-1] * i % mod)
(*p,) = list(range(n))
r = [0] * n


def par(x):
    if p[x] == x:
        return x
    res = p[x] = par(p[x])
    return res


def union(x, y):
    px = par(x)
    py = par(y)
    if px == py:
        return
    if r[px] > r[py]:
        p[py] = px
        r[py] += 1
    elif r[px] < r[py]:
        p[px] = py
        r[px] += 1
    else:
        p[px] = py
        r[py] += 1


for i in range(n):
    for j in range(i):
        chng = True
        for t in range(n):
            if a[i][t] + a[j][t] > k:
                chng = False
                break
        if chng:
            union(i, j)
for i in range(n):
    par(i)
ans = 1
Cp = Counter(p)
for g in Cp:
    ans *= f[Cp[g]]
    ans %= mod
(*p,) = list(range(n))
r = [0] * n
for i in range(n):
    for j in range(i):
        chng = True
        for t in range(n):
            if a[t][i] + a[t][j] > k:
                chng = False
                break
        if chng:
            union(i, j)
for i in range(n):
    par(i)
Cp = Counter(p)
for g in Cp:
    ans *= f[Cp[g]]
    ans %= mod
print(ans)
