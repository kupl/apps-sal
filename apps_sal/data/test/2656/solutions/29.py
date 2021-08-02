K = int(input())
S = input()
N = len(S)
mod = int(1e9 + 7)


wk = pow(26, K, mod)
inv26 = pow(26, -1, mod)

ans = wk
for i in range(1, K + 1):
    wk = (wk * 25 * inv26) % mod
    wk = (wk * (N - 1 + i) * pow(i, -1, mod) % mod)
    ans = (ans + wk) % mod

print(ans)
