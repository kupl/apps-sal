k = int(input())
s = input()
n = len(s)

MAX = 10**6
MOD = 10**9 + 7

inv = [0] * (MAX + 1)
inv[1] = 1
for i in range(2, MAX + 1):
    q, r = divmod(MOD, i)
    inv[i] = -inv[r] * q % MOD

ans = val = pow(26, k, MOD)
for i in range(1, k + 1):
    val *= (i + n - 1) * 25 * inv[i] * inv[26] % MOD
    val %= MOD
    ans += val
    ans %= MOD
print(ans)
