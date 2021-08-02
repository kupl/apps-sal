n = int(input())
M = 998244353

ans = 1

fac = 1
phi = 1

for q in range(n, 2, -1):
    fac *= q
    fac %= M
    phi += fac
    phi %= M

fac *= 2
fac %= M

ans += fac * (n - 1)
ans %= M

ans += M - phi
ans %= M

if n == 1:
    ans = 1

print(ans)
