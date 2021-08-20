(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
aj = 0
xsum = 0
(mod1, mod2) = (10 ** 9 + 7, 998244353)
mod = mod1
for j in range(1, n):
    aj = (aj + j * (x[j] - x[j - 1]) % mod) % mod
    xsum = (xsum + aj) % mod
bj = 0
ysum = 0
for j in range(1, m):
    bj = (bj + j * (y[j] - y[j - 1]) % mod) % mod
    ysum = (ysum + bj) % mod
print(xsum * ysum % mod)
