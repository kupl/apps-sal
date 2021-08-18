
N, K = map(int, input().split())
L_R = [list(map(int, input().split())) for _ in range(K)]


MOD = 998244353
L_R.sort()

f = [0] * N
f[0] = 1
a = [0] * (N + 1)
a[1] = -1

for i in range(N - 1):
    for l, r in L_R:
        if i + l < N:
            a[i + l] += f[i]
            a[i + l] %= MOD
        if i + r + 1 < N:
            a[i + r + 1] -= f[i]
            a[i + r + 1] %= MOD
    f[i + 1] = (f[i] + a[i + 1]) % MOD

print(f[-1])
