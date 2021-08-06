MOD = 998244353

n = int(input())
d = [0] * n
a = list(map(int, input().split()))
for i in range(n - 2, -1, -1):
    if (a[i] <= 0):
        continue
    cur_cnk = 1
    cur_k = a[i]
    cur_n = a[i]
    for j in range(i + a[i] + 1, n):
        d[i] = (d[i] + d[j] * cur_cnk % MOD) % MOD
        cur_cnk *= (cur_n + 1)
        cur_cnk //= (cur_n + 1 - cur_k)
        cur_n += 1
    if (i + a[i] + 1 <= n):
        d[i] = (d[i] + cur_cnk) % MOD
ans = 0
for i in range(n):
    ans = (ans + d[i]) % MOD
print(ans)
