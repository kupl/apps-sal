n, m, k = map(int, input().split())
mod = 10 ** 9 + 7

res_n = 0
for i in range(1, n+1):
    res_n += (n + 1 - i) * (n - i) // 2
    res_n %= mod
res_n = (res_n * (m ** 2)) % mod

res_m = 0
for i in range(1, m+1):
    res_m += (m + 1 - i) * (m - i) // 2
    res_m %= mod
res_m = (res_m * (n ** 2)) % mod

res = res_n + res_m
#print(res)

f = [1 for _ in range(n*m)]
for i in range(1, n*m):
    f[i] = f[i-1] * i % mod

res = res * f[n*m-2] * pow(f[k-2], mod-2, mod) * pow(f[n*m-k], mod-2, mod) % mod

print(res)
