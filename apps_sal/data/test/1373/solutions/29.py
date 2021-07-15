n, k = map(int, input().split())

MOD = 10**9+7
n += 1
ans = 0
for i in range(k, n+1):
    p = i*(2*n - (i-1)) // 2
    m = i*(2 + i-1) // 2
    ans += p - m + 1
print(ans % MOD)
