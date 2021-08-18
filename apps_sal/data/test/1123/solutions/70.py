N, K = list(map(int, input().split()))
MOD = 10**9 + 7


ans = 0
gcds = [0] * (K + 1)
for i in reversed(list(range(1, K + 1))):
    gcds[i] = pow(K // i, N, MOD)
    idx = i * 2
    while idx < K + 1:
        gcds[i] -= gcds[idx] + MOD
        gcds[i] %= MOD
        idx += i
    ans += (i * gcds[i])
    ans %= MOD


print(ans)
