n = int(input())
a = [int(x) for x in input().strip().split()]
mod = 998244353
ans = 0

g = [1, 2]
p = 1

while len(g) < n:
    h = g[-1] * 2 + p
    p *= 2
    if p > mod:
        p %= mod
    if h > mod:
        h %= mod
    g.append(h)

for i in range(n):
    if i > 0:
        a[i] = (a[i] + a[i - 1]) % mod
    ans += a[i] * g[n-1-i]
    if ans > mod:
        ans %= mod

print(ans)

