(N, K) = list(map(int, input().split()))
mod = 10 ** 9 + 7
fact_count = [0 for _ in range(K + 1)]
for k in range(1, K + 1):
    fact_count[k] = K // k
ans = 0
count = [0 for _ in range(K + 1)]
for k in range(K, 0, -1):
    c = pow(fact_count[k], N, mod)
    j = 2 * k
    l = 2
    while j <= K:
        c -= count[j]
        l += 1
        j = k * l
    count[k] = c
    c = c * k % mod
    ans += c
    ans %= mod
print(ans)
