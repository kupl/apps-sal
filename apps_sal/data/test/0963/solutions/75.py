n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353
dp = [0] * (n + 1)
imos = [0] * (n + 1)

for i in range(n):
    if i == 0:
        tmp = 1
    else:
        imos[i] = (imos[i] + imos[i - 1]) % mod
        tmp = imos[i]
    for j in range(k):
        if lr[j][0] + i > n:
            continue
        imos[lr[j][0] + i] += tmp
        imos[min(lr[j][1] + 1 + i, n)] -= tmp
print(imos[-2] % mod)
