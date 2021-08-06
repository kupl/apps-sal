n, k = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]


def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]


def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1


def Same(x, y, par):
    return Find(x, par) == Find(y, par)


def Size(x, par):
    return -par[Find(x, par)]


par1 = [-1] * n
rank1 = [0] * n
for x in range(n):
    for y in range(n):
        for i in range(n):
            if A[x][i] + A[y][i] > k:
                break
        else:
            Unite(x, y, par1, rank1)

par2 = [-1] * n
rank2 = [0] * n
for x in range(n):
    for y in range(n):
        for i in range(n):
            if A[i][x] + A[i][y] > k:
                break
        else:
            Unite(x, y, par2, rank2)

N = 1000
mod = 998244353
fac = [1] * (N + 1)
finv = [1] * (N + 1)
for i in range(N):
    fac[i + 1] = fac[i] * (i + 1) % mod
finv[-1] = pow(fac[-1], mod - 2, mod)
for i in reversed(list(range(N))):
    finv[i] = finv[i + 1] * (i + 1) % mod

ans = 1
for i in par1:
    if i < 0:
        ans *= fac[-i]
        ans %= mod
for i in par2:
    if i < 0:
        ans *= fac[-i]
        ans %= mod
print(ans)
