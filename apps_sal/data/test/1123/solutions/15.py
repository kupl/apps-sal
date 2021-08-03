n, k = map(int, input().split())
mod = 10**9 + 7
"""
dp[i] := gcd(a1,...,an) = i となるものがいくつあるか
"""
dp = [0 for _ in range(k + 1)]
subdp = [0 for _ in range(k + 1)]
for i in range(1, k + 1)[::-1]:
    target = pow(k // i, n, mod)
    for j in range(2 * i, k + 1, i):
        target -= dp[j]
    dp[i] = target
ans = 0
for i in range(k + 1):
    ans = (ans + dp[i] * i) % mod
print(ans)
