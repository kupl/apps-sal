MOD = 10 ** 9 + 7
(n, k) = map(int, input().split())
mp = [0] * (k + 1)
for i in range(k, 0, -1):
    mp[i] = pow(k // i, n, MOD)
    t = 2
    while i * t <= k:
        mp[i] -= mp[t * i]
        t += 1
ans = 0
for i in range(1, k + 1):
    ans += i * mp[i]
print(ans % MOD)
