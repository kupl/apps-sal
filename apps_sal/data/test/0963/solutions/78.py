N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
mod = 998244353

z = [1] + [0] * (N - 1)
s = [0] * (N + 2)
for j in range(N):
    for l, r in LR:
        z[j] += s[j - l] - s[j - r - 1]
    s[j] = (s[j - 1] + z[j]) % mod

print(z[-1] % mod)
