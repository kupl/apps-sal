import math
def lca(a, b): return a * b // math.gcd(a, b)


mod = 1000000007
m = int(input())
ps = list(map(int, input().split()))
cnt = {}
for p in ps:
    if p not in cnt:
        cnt[p] = 0
    cnt[p] += 1
lca_i = 1
k = 1
for i in list(cnt.values()):
    k *= i + 1
    lca_i = lca(lca_i, i + 1)
ans = 1
for p, i in list(cnt.items()):
    ans = ans * pow(p, i * (i + 1) // 2 * lca_i // (i + 1), mod) % mod
ans = pow(ans, k // lca_i, mod)
print(ans)
