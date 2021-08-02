m = 998244353
n = int(input())
f = [0 for i in range(n + 1)]
ff = [0 for i in range(n + 1)]
f[1] = 1
ff[n] = n
for i in range(2, n + 1):
    f[i] = (f[i - 1] % m * i % m) % m

for i in range(n - 1, 1, -1):
    ff[i] = (ff[i + 1] % m * i % m) % m

ans = (f[n] % m * n % m) % m

for i in range(2, n + 1, 1):
    ans = (ans % m + (-1 * ff[i] % m) % m) % m
print(ans)
