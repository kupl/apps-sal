k = int(input())
s = input()
n = len(s)

MOD = 10**9 + 7
d = pow(26, -1, MOD)
ans = val = pow(26, k, MOD)
for i in range(1, k + 1):
    val *= (i + n - 1) * 25 * pow(i, -1, MOD) * d % MOD
    val %= MOD
    ans += val
    ans %= MOD
print(ans)
