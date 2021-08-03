import sys
input = sys.stdin.readline
n, k = map(int, input().split())
mod = 998244353
fac = [1] * n
for i in range(1, n):
    fac[i] = i * fac[i - 1]
    fac[i] %= mod
i = 1
sol = 0
while ((n - i) // i) >= (k - 1):
    mul = fac[(n - i) // i]
    div = fac[k - 1]
    div *= fac[1 + (n - i) // i - k]
    div %= mod
    s = pow(div, mod - 2, mod)
    s *= mul
    s %= mod
    sol += s
    sol %= mod
    i += 1
print(sol)
