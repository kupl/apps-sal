n = int(input())
ar = list(map(int, input().split()))
ar.sort()
MOD = 10**9 + 7
ans = 0
for i in range(n):
    bef = i
    aft = n - i - 1
    if bef < aft:
        ans -= (ar[i] * (pow(2, aft, MOD) - pow(2, bef, MOD) + MOD) % MOD)
        ans %= MOD
    elif aft < bef:
        ans += (ar[i] * (pow(2, bef, MOD) - pow(2, aft, MOD) + MOD) % MOD)
        ans %= MOD
print(ans)
