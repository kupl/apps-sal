(N, K) = list(map(int, input().split()))
mod = 10 ** 9 + 7
cnt = [0] * (K + 1)
ans = 0
for g in range(K, 0, -1):
    sub = sum(cnt[2 * g:K + 1:g])
    q = pow(K // g, N, mod) - sub
    ans = (ans + g * q) % mod
    cnt[g] = q
print(ans)
