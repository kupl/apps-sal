import sys
K = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip('\n')
N_MAX = 10 ** 6
MOD = 10 ** 9 + 7
inv = [0] * (N_MAX + 2)
inv[0] = 0
inv[1] = 1
for i in range(2, N_MAX + 2):
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
ans = 0
ln = len(S)
p1 = 1
p2 = 1
s2 = pow(26, K, MOD)
for i in range(1, K + 2):
    ans += p1 * p2 * s2 % MOD
    ans %= MOD
    p1 = p1 * (ln + i - 1) * inv[i] % MOD
    p2 = p2 * 25 % MOD
    s2 = s2 * inv[26] % MOD
print(ans)
