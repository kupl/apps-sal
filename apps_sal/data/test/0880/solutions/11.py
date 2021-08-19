n = int(input())
mod = 998244353
rev = []
cur = 1
s = 0
for i in range(n, 0, -1):
    cur *= i
    tmp = cur - s
    s += tmp
    s %= mod
    cur %= mod
    rev.append(tmp % mod)
ans = 1
for i in range(1, n + 1):
    ans *= i
    ans %= mod
for i in range(1, n - 1):
    ans += i * rev[i]
    ans %= mod
print(ans)
