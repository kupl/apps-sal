N, *A = map(int, open(0).read().split())
mod = 10**9 + 7

batch = 8
rg = tuple(range((63//batch)+1))
mask = (1<<batch) - 1
B = [[0]*(1<<batch) for _ in rg]
for a in A:
    for i in rg:
        B[i][a & mask] += 1
        a >>= batch

xr = [[] for _ in [0]*(1<<batch)]
for i in range(1<<batch):
    for j in range(i+1, 1<<batch):
        xr[i].append(i^j)

ans = 0
shift = 1
for b in B:
    x = sum(xr[i][j]*bi*bj for i, bi in enumerate(b) for j, bj in enumerate(b[i+1:]))
    x %= mod
    x *= shift
    x %= mod
    shift <<= batch
    shift %= mod
    ans += x
    ans %= mod
print(ans)
